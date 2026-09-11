class Necromancer:

    def __init__(self, name, resource, max_controlled_undead):
        from resource import Resource
        self.__resource = Resource()
        self.__max_controlled_undead = 5
        self.__undead = []

    def get_resource(self):
        return self.__resource

    def perform_summoning_ritual(self, ritual):
        if sum(slot is not None for slot in self.__undead) < self.__max_controlled_undead:  # if too many undead
            return
        if not ritual.can_be_performed_with_resources(self.__resource):
            return
        ritual.consume_resources(self.__resource)
        id = self.__undead.index(None)
        self.__undead[id](ritual.create_undead(5))
        return id

    def dismiss_undead(self, id):
        self.get_undead_from_id[id].__del__()
        self.__undead[id] = None

    def get_undead_from_id(self, id):
        return self.__undead[id]

    def level_up_undead(self, id):
        self.get_undead_from_id(id).increase_level()

    resource = property(get_resource)
