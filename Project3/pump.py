from Pipe import Pipe
from Ticking import Ticking


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
        Ticking.__init__(self)
        self.static_pressure = static_pressure
        self.max_speed = max_speed
        self.throttle = 0

    def on_update(self, delta_time):
        """ Apply pump pressure to flow component. """
        self.flow_component.h_pump = self.get_pump_pressure(
            self.flow_component.velocity)/(self.flow_component.fluid.density*9.81)

    def get_pump_pressure(self, v):
        """ Helper function. Simulates the velocity-dependent performance curve of a pump. """
        return (self.throttle*self.static_pressure*(self.max_speed-v)**(3/11)) / \
            (self.max_speed**(3/11))
