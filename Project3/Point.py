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
        self.pressure = 0  # Approx atmostpheric pressure in Pa.
        # Whether the pressure is set or can change.
        self.is_endpoint = False
        self.__connections = []

    def add_connection(self, new_connection):
        if isinstance(new_connection, Point) or isinstance(new_connection, list):
            raise (TypeError(f"???? : {new_connection}"))
        self.__connections.append(new_connection)

    def remove_connections(self, connection):
        self.__connections.remove(connection)
        if not self.__connections:  # Delete "orphaned" points.
            del self

    connections = property(lambda self: self.__connections, None)
