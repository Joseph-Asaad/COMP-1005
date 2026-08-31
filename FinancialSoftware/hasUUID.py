import uuid as uuid  # UUID library


class hasUUID:
    """
    An abstract class that registers a constant, unique UUID for objects of derived classes; allows searching for objects by UUID.

    Methods
    -------
    get_ID : uuid
        returns the object's UUID.
    set_ID(uuid) : void
        allows for setting of a uuid if the object does not already have one.
    static get_from_UUID(uuid) : hasUUID
        returns object which has supplied UUID.
    """

    UUID_objects = []  # Central registry of everything with a UUID.

    def get_ID(self):  # ID getter.
        return self._UUID

    # ID setter. IDs are immutable cannot be changed, only added to objects without IDs.
    def set_ID(self, uuid=uuid.uuid4()):
        if (not hasattr(self, '_UUID')) or self._UUID == None:
            self._UUID = uuid

    @classmethod
    def __init__(cls, self):
        self.set_ID()
        cls.UUID_objects.append(self)  # add to registry.

    @classmethod
    def get_from_UUID(cls, uuid):  # Search registry for an object.
        for i in cls.UUID_objects:
            if i._UUID == uuid:
                return i
