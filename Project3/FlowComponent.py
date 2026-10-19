from math import sqrt, log10, pi


class FlowComponent:

    flow_components = []  # Central registry of every FlowComponent.

    def __init__(self, length, radius, fluid, pipe, ends, roughness):
        cls = self.__class__
        self.pipe = pipe
        self.fluid = fluid
        self.length = length
        self.radius = radius
        self.roughness = roughness

        self.velocity = 0

        self.h_pump = 0

        # Create association between pipe and both end points.
        self.ends = ends
        for end in ends:
            end.add_connection(ends)

        cls.flow_components.append(self)  # Add to registry.

    vol_flow_rate = property(
        lambda self: self.velocity * pi * self.radius**2, None)
    mass_flow_rate = property(
        lambda self: self.fluid.density * self.vol_flow_rate, None)

    def __del__(self):
        cls = self.__class__
        cls.flow_components.remove(self)  # Remove from registry on deletion.
        del self

    @classmethod
    def simulate(cls, delta_time):  # Update state.
        print("Simulating")

        for FC in cls.flow_components:
            # Calculate Reynolds Number.
            Re = (FC.fluid.density * FC.velocity *
                  FC.pipe.length)/FC.fluid.viscosity

            # Friction factor.
            f = cls.Colebrook_White(Re, FC.roughness, 2*FC.radius)

            # Find difference in pressure (dp) from end 0 to end 1 due to each factor.

            # Darcy-Weissback Equation.
            dp_friction = (f*FC.fluid.density*FC.velocity**2)/(4*FC.radius)
            # rho g h
            dp_gravity = FC.fluid.density*9.81 * \
                FC.ends[1].coords[2]-FC.ends[0].coords[2]
            dp_external = FC.ends[1]

            # Mechanical Energy Equation.
            E_0 = FC.ends[0].pressure / \
                (FC.fluid.density * 9.81) + FC.ends[0].coords[2] + FC.h_pump
            E_2 = (FC.fluid.density * 9.81) + FC.ends[0].coords[2] + FC.h_loss

    @staticmethod
    def Colebrook_White(Re, roughness, D):
        """
        Iteratively solve the Colebrook-White equation to find f within a tolerance of 0.001x, or about 1%
        """
        diff = 1
        f = 0.02  # Initial guess
        while diff > 0.001:
            f_old = f
            f = (-2*log10(roughness/(3.7*D) + 2.5/(Re*sqrt(f))))**-2
            diff = abs(f-f_old)
        return f
