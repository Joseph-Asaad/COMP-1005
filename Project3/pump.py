from Pipe import Pipe
from Ticking import Ticking
from math import nth


class Pump(Pipe, Ticking):
    def __init__(self, length, radius, ends, roughness, static_pressure, max_speed):
        super().__init__(length, radius, ends, roughness)
        self.static_pressure = static_pressure
        self.max_speed = max_speed

    def onUpdate(self, delta_time):
        """ Simulates the velocity-dependent performance curve of a pump."""
        rho = self.flow_component.fluid.density
        v = self.flow_component.velocity
        self.flow_component.h_pump = (
            self.static_pressure*(self.max_speed-v)**0.25)*(rho*9.81*self.max_speed**0.25)
