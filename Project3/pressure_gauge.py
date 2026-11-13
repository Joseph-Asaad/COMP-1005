from Gauge import Gauge


class PressureGauge(Gauge):
    def readout(self):
        return f"Pressure: {self.midpoint.pressure/1000:.1f} kPa"
