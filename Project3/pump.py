from Pipe import Pipe
from Ticking import Ticking


class Pump(Pipe, onUpdate):
    def __init__(self, length, radius, ends, roughness, performance_curve: function):
        self.performance_curve = performance_curve
        super().__init__(length, radius, ends, roughness)

    def onUpdate(self, delta_time):
        self._heat_component.h_pump = self.performance_curve(
            self._flow_component.vol_flow_rate)
