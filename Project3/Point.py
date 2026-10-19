class Point:

    def __init__(self, coords):
        self.coords = coords  # Coordinates as [x, y, z].
        self.pressure = 100000  # Approx atmostpheric pressure.
        self._connections = []

    def add_connection(self, new_connection):
        self._connections.append(new_connection)

    def remove_connections(self, connection):
        self._connections.remove(connection)
        if not self._connections:
            del self

    connections = property(lambda self: self._connections, None)
