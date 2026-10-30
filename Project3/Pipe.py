from FlowComponent import FlowComponent


class Pipe:

    def __init__(self, radius, fluid, ends, roughness, length=None):
        self.flow_component = FlowComponent(
            radius, fluid, ends, roughness, length)
