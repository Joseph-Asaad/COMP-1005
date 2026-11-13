from Gauge import Gauge


class pressure_gauge(Gauge):
    def readout(self):
        return f"Pressure: {self.midpoint.pressure/1000:.1f} kPa"
