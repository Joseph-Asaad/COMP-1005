from Pipe import Pipe
from Ticking import Ticking
from math import nth


class Pump(Pipe, Ticking):
    """
    A pump. It pumps fluid from the start point to the end point according to its parameters.

    Attributes
    ----------
    _static_pressure : num
        The pressure the pump can produce when the velocity is zero.
    """

    def __init__(self, radius, fluid, ends, roughness, static_pressure, max_speed, length=None):
        super().__init__(radius, fluid, ends, roughness, length)
        self.static_pressure = static_pressure
        self.max_speed = max_speed
        self.throttle = 0

    def onUpdate(self, delta_time):
        """ Simulates the velocity-dependent performance curve of a pump."""
        rho = self.flow_component.fluid.density
        v = self.flow_component.velocity
        self.flow_component.h_pump = \
            (self.static_pressure*(self.max_speed-v)**(3/11)) / \
            (rho*9.81*self.max_speed**(3/11))
