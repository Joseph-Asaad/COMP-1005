class Fluid:
    """
    A fluid material, not a quantum of fluid.

    Attributes
    ----------
    density : num
        The density in kg/m3 of the fluid.

    viscosity : num
        The dynamic viscosity of the fluid.

    kinematic_viscosity : num
        The kinematic viscosity of the fluid - read only.

    """

    def __init__(self, density, viscosity):
        self.density = density
        self.viscosity = viscosity

    kinematic_viscosity = property(
        lambda self: self.viscosity/self.density, None)
