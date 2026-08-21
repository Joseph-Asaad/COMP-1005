import uuid as uuid
class hasUUID : 

  UUID_objects = []

  def get_ID (self) : 
    return self._UUID

  def set_ID (self, uuid = uuid.uuid4()) : 
    if self._UUID == None : 
      self._UUID = uuid

  @classmethod
  def __init__ (cls, self) : 
    self.__uuid = uuid.uuid4()
    cls.UUID_objects.extend(self)

  @classmethod
  def get_from_UUID (cls, uuid) :
    for i in cls.UUID_objects :
      if i._UUID == uuid :
        return i