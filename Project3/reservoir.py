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
        self.__fluid_height = 0
        self.fill_rate = 0

    def __delete__(self, instance):
        self.point.remove_connection(self)

    area = property(
        lambda self: pi * self.radius**2, None)

    volume = property(lambda self: self.area * self.fluid_height)

    def get_fluid_height(self):
        return self.__fluid_height

    def set_fluid_height(self, height):
        self. __fluid_height = height
        self.on_update(None)

    fluid_height = property(get_fluid_height, set_fluid_height)

    def on_update(self, delta_time):
        self.point.pressure = 9.81 * self.fluid.density * self.fluid_height
