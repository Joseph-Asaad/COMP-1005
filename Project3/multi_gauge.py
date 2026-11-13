from pressure_gauge import PressureGauge
from flow_gauge import FlowGauge


class MultiGauge(PressureGauge, FlowGauge):
    def readout(self):
        return f"{super.readout()}, {FlowGauge.readout(self)}"
