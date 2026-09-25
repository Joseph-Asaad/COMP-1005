from math import sqrt, log10


class FlowComponent:

    flow_components = []  # Central registry of every FlowComponent.

    @classmethod
    def __init__(cls, self, length, radius, fluid, pipe, ends, roughness):
        self.pipe = pipe
        self.fluid = fluid
        self.length = length
        self.ends = ends
        self.radius = radius
        self.roughness = roughness
        cls.flow_components.append(self)  # Add to registry.

    @classmethod
    def __del__(cls, self):
        cls.flow_components.remove(self)  # Remove from registry on deletion.
        del self

    @classmethod
    def simulate(cls, delta_time):  # Update state.
        for FC in cls.flow_components:
            # Calculate Reynolds Number.
            Re = (FC.fluid.density * FC.velocity *
                  FC.pipe.length)/FC.fluid.viscosity

            if Re < 4000:  # Laminar.
                pass
            else:  # Turbulent.
                f = cls.Colebrook_White(Re, FC.roughness, 2*FC.radius)

    @staticmethod
    def Colebrook_White(Re, roughness, D):
        diff = float.inf
        f = 0.02  # Initial guess
        while diff > 0.001:
            f = (-2*log10(roughness/(3.7*D) + 2.5/(Re*sqrt(f))))**-2
        return f
