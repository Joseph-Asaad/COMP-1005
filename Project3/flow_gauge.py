from Gauge import Gauge


class FlowGauge(Gauge):

    def readout(self):
        return f"Flow Rate: {0.001*self.pipe_1.flow_component.velocity*self.pipe_1.flow_component.area} L/s"
