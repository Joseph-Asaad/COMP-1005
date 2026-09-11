class SummoningRitual:
    from typing import Type
    from undead import Undead

    def __init__(self, undead_type: Type[Undead], ritual_name, undead_name, initial_health, initial_power, resource_cost: int[5]):
        from resource import Resource
        if resource_cost[Resource.ResourceTypes.ECTOPLASM.value[1]] < 1:
            raise (ValueError)
        self.__resource_cost = resource_cost
        self.initial_health = initial_health
        self.initial_power = initial_power
        self.__ritual_name = ritual_name
        self.__undead_name = undead_name
        self.__undead_type = undead_type

    def can_be_performed_with_resources(self, resource):
        return (resource.subtract_resource(self.__resource_cost, False))

    def _consume_resources(self, resource):
        return (resource.subtract_resource(self.__resource_cost, True))

    def create_undead(self, id):
        from undead import Undead
        return self.__undead_type.__init__(id, self.initial_health, self.initial_power)
