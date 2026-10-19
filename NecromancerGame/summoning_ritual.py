class SummoningRitual:
    """
    This class represents a summoning ritual.

    Methods
    -------
    can_be_performed_with_resources (resource : Resource) : bool
        Returns True when [resource] has sufficient resources to perform this summoning ritual.
    
    consume_resources(resource: Resource) : void
        Subtracts this ritual's cost from the provided resource object.

    create_undead(id : int) : Undead
        Returns a new Undead with the provided ID.

    Attributes
    ----------

    __resource_cost : tuple(int, int, int, int, int)
    initial_health : int
    initial_power : int
    __ritual_name : str
    __undead_name : str
    __undead_type : class(Undead)
    """
    from typing import Type
    # TODO : check this works to be sure

    def __init__(self, undead_type: Type[Undead], ritual_name: str, undead_name: str, initial_health: float, initial_power: float, resource_cost: tuple[int, int, int, int, int]):
        from resource_handler import Resource
        from undead_classes.undead import Undead
        if not (isinstance(undead_type, type) and issubclass(undead_type, Undead)):
            raise (TypeError)
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

    def consume_resources(self, resource):
        return (resource.subtract_resource(self.__resource_cost, True))

    def create_undead(self, id):
        return self.__undead_type(id, self.initial_health, self.initial_power)

    def get_undead_type(self):
        return self.__undead_type

    undead_type = property(get_undead_type)
