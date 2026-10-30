from Ticking import Ticking
from math import pi


class Reservoir(Ticking):
    def __init__(self, point, radius, fluid):
        Ticking.__init__(self)
        self.point = point
        self.point.is_endpoint = True
        self.point.add_connection(self)

        self.radius = radius
        self.fluid = fluid
        self.fluid_height = 0
        self.fill_rate = 0

    area = property(
        lambda self: pi * self.radius**2, None)

    volume = property(lambda self: self.area * self.fluid_height)

    def on_update(self, delta_time):
        self.point.pressure = self.fluid.density * self.fluid_height
