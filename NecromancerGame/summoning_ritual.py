class SummoningRitual:

    def __init__(self, resource_cost):
        from resource import Resource
        if resource_cost[Resource.ResourceTypes.ECTOPLASM] < 1:
            raise (ValueError)
        self.__resource_cost = resource_cost
