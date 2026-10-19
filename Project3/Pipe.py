from FlowComponent import FlowComponent


class Pipe:

    def __init__(self, length, radius, ends, roughness):
        self._flow_component = FlowComponent(
            length, radius, None, None, ends, roughness)
