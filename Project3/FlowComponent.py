from math import sqrt, log10, pi, copysign
from Ticking import Ticking
from Point import Point
import numpy as np


@Ticking.TickingClass
class FlowComponent(Ticking):

    flow_components = []  # Central registry of every FlowComponent.

    def __init__(self, radius, fluid, ends, roughness, length=None):
        cls = self.__class__
        self.fluid = fluid
        self.length = length if length != None else np.sqrt(
            (ends[0].coords[0]-ends[1].coords[0])**2 + (ends[0].coords[1]-ends[1].coords[1])**2 + (ends[0].coords[2]-ends[1].coords[2])**2)
        self.radius = radius
        self.roughness = roughness

        self.velocity = 0
        self.acceleration = 0

        self.h_pump = 0

        # Create association between flow component and both end points.
        self.ends = ends
        for end in ends:
            end.add_connection(self)

        cls.flow_components.append(self)  # Add self to registry.

    area = property(
        lambda self: pi * self.radius**2, None)

    vol_flow_rate = property(
        lambda self: self.velocity * self.area, None)

    mass_flow_rate = property(
        lambda self: self.fluid.density * self.vol_flow_rate, None)

    def __del__(self):
        cls = self.__class__
        cls.flow_components.remove(self)  # Remove from registry on deletion.
        del self

    @classmethod
    def on_update(cls, delta_time):  # Update state.
        """
        Runs one simulation step.
        """
        # Uses a linear system of the following equations:
        #
        # For each flow component, p1 - p0 - f(accel) = const, as per mechancial energy equation.
        # For each point, Sum(Area * accel) = 0 for each connection as per continuity equation.
        # For each point connected to a reservoir, p = const depending on reservoir pressure.
        #

        points = []  # Create and populate a dict of each point.
        # Assign an order from 0...n to each point
        for FC in cls.flow_components:
            for end in FC.ends:
                if not end in points:
                    points.append(end)

        # Create augmented matrix for linear equation solving, Ax = B.
        # Structure of x: Point pressures | Flow Component accelerations | Reservoirs and outlets.
        X = points + cls.flow_components
        A = []
        B = []

        # Create equations corresponding to each flow component
        for FC in cls.flow_components:
            # Calculate Reynolds Number.
            Re = (FC.fluid.density * abs(FC.velocity) *
                  2*FC.radius)/FC.fluid.viscosity

            # Friction factor.
            f = cls.Colebrook_White(Re, FC.roughness, 2*FC.radius)

            # Find difference in pressure (dp) from end 0 to end 1 due to each factor.

            # Darcy-Weissback Equation.
            dp_friction = (f*FC.fluid.density*FC.velocity**2)/(4*FC.radius)
            h_loss = FlowComponent.sign(FC.velocity)*dp_friction / \
                (FC.fluid.density * 9.81)

            # Find the pressure difference due to inertia
            p_inertia = FC.length*FC.fluid.density  # * dV/dt

            h_height = (FC.ends[1].coords[2] - FC.ends[0].coords[2])

            # Mechanical Energy Equation for p1 - p0 = rho*g*(z -h_loss + h_pump) + rho*L*dV/dt
            # therefore p1 - p0 - rho*L*(dV/dt) - rho*g*(z -h_loss + h_pump) = 0
            dp = FC.fluid.density * 9.81 * (h_height - h_loss + FC.h_pump)

            # Construct the row of the matrix for this equation.
            # Find indeces of each term in the left-hand-side.
            [ip_0, ip_1, iFC] = [X.index(FC.ends[0]),
                                 X.index(FC.ends[1]),
                                 X.index(FC)]

            LHS = [0] * len(X)
            LHS[ip_1] = 1
            LHS[ip_0] = -1
            LHS[iFC] = p_inertia

            A.append(LHS.copy())
            B.append(dp)

        # Create equations corresponding to each point.
        for pt in points:

            # Endpoints import/export fluid and have a known pressure.
            if pt.is_endpoint:
                # "Bonus" equation -p + p.pressure = 0 to set pressure.
                LHS = [0] * len(X)
                LHS[X.index(pt)] = -1
                A.append(LHS.copy())
                B.append(-pt.pressure)

            # Sum of flows into this point equals 0 as per conservation of mass.
            LHS = [0] * len(X)
            B.append(0)

            for connection in pt.connections:  # Sum up in/outflows to point
                from reservoir import Reservoir
                match connection.__class__.__name__:
                    case Reservoir.__name__:
                        # Create new unknown variable for reservoir in/outflow.
                        X.append(connection)
                        LHS.append(0)
                        # Increase size of A matrix to keep it square
                        for row in A:
                            row.append(0)
                        LHS[X.index(connection)] = connection.area

                    case FlowComponent.__name__:
                        # Index in the A matrix of this connection
                        index = X.index(connection)

                        # Flow direction from p0 to p1.
                        match connection.ends.index(pt):
                            case 0:  # This is the first point, flow is away from this point.
                                LHS[index] = -1*connection.vol_flow_rate
                            case 1:  # This is the second point, flow is towards this point.
                                LHS[index] = +1*connection.vol_flow_rate
                    case _:
                        raise (TypeError(
                            f"Invalid connection type: {connection} is of invalid type {connection.__class__.__name__}"))
            A.append(LHS)
        # Use numpy for now to get numerical results because I can't be stuffed.
        Xprime = np.linalg.solve(A, B)  # Solve linear system.

        # Update based on results.
        for [i, result] in enumerate(Xprime):
            obj = X[i]
            if isinstance(obj, Point):  # Update point pressure.
                obj.pressure = result

            elif isinstance(obj, FlowComponent):  # Accelerate flow.
                obj.velocity += result*delta_time

            elif isinstance(obj, Reservoir):  # Fill/Empty reservoir.
                obj.fluid_height += (0.5*result*delta_time**2 +
                                     obj.fill_rate*delta_time)
                obj.fill_rate += result * delta_time

    @staticmethod
    # Helper function for Colebrook-White Equation.
    def Colebrook_White(Re, roughness, D):
        """
        Iteratively solve the Colebrook-White equation to find f within a tolerance of 0.001x, or about 1%
        """
        if Re == 0:  # Begone div/0 errors!
            return 0
        diff = 1
        f = 0.02  # Initial guess
        while diff > 0.00001:
            f_old = f
            f = (-2*log10(roughness/(3.7*D) + 2.5/(Re*sqrt(f))))**-2
            diff = abs(f-f_old)
        return f

    # Helper function that could easily be replaced with numpy but we can't use external libraries so I guess I'll implement this myself.
    def linsolve(coefficients):
        pass

    def sign(x):
        """ Returns the sign of the input, -1, 0, or 1"""
        return copysign(1, x)
