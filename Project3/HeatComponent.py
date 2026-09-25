class HeatComponent:

    heat_components = []  # Central registry of every HeatComponent.

    @classmethod
    def __init__(cls, self, material, cross_sectional_area, length):
        self.material = material
        self.cross_sectional_area = cross_sectional_area
        self.length = length
        cls.heat_components.append(self)  # add to registry.

    @classmethod
    def __del__(cls, self):
        cls.heat_components.remove(self)

    @classmethod
    def simulate(cls):
        pass
