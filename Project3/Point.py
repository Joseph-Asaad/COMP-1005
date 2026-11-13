from math import isnan


class Point:
    """
    A point in space that can be connected to by pipes, reservoirs, etc.

    Attributes
    ----------
    coords : [num num num]
        x,y,z coordinates of the point. Not neccesarily unique.

    pressure : 
        Absolute hydrodynamic pressure at this point.

    is_set_pressure : bool
        Whether the pressure is fixed (e.g. by an outlet or reservoir) or should be calculated by the system.

    connections : list []
        List of FlowComponents etc. that are connected to this point, used for conservation of mass calculations.

    Methods
    -------
    add_connection(new_connection) : void
        adds a connection

    remove_connection(connection) : void
        removes a connection, will automatically delete self when last connection is removed.

    """

    def __init__(self, coords):
        self.coords = coords  # Coordinates as [x, y, z].
        self.__pressure = 0  # Approx atmostpheric pressure in Pa.
        # Whether the pressure is set or can change.
        self.is_endpoint = False
        self.__connections = []

    def add_connection(self, new_connection):
        from reservoir import Reservoir
        if isinstance(new_connection, Point) or isinstance(new_connection, list):
            raise TypeError

        # Enforce the 1:1 multiplicity of reservoirs.
        if isinstance(new_connection, Reservoir) and any(isinstance(connection, Reservoir) for connection in self.connections):
            raise MultiplicityError(
                f"Point {self} already attached to Reservoir {next(connection for connection in self.connections if isinstance(connection, Reservoir))}")

        self.__connections.append(new_connection)

    def remove_connections(self, connection):
        self.__connections.remove(connection)

    connections = property(lambda self: self.__connections, None)

    def set_pressure(self, new_pressure):
        if isnan(new_pressure):
            raise ValueError("Cannot be NaN.")
        self.__pressure = new_pressure

    def get_pressure(self):
        return self.__pressure

    pressure = property(get_pressure, set_pressure)

    def get_inflow_surplus(self):
        """ Returns the vol. flow rate of the "extra" fluid flowing into the point that should be taken up by a reservoir. Positive value -> excess fluid."""
        out = 0
        for connection in self.connections:
            from FlowComponent import FlowComponent
            if not isinstance(connection, FlowComponent):
                continue
            if self == connection.ends[0]:
                out -= connection.vol_flow_rate
            else:
                out += connection.vol_flow_rate
        return out


class MultiplicityError(Exception):
    def __init__(self, message):
        self.message = message
        super().__init__(self.message)
