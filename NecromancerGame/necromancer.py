class Necromancer:
    from resourceHandler import Resource
    from summoning_ritual import SummoningRitual

    def __init__(self, name: str, max_controlled_undead: int):
        # pyright: ignore[reportAttributeAccessIssue]
        from resourceHandler import Resource
        self.__resource = Resource()
        self.__max_controlled_undead = 5
        self.__undead = [None] * max_controlled_undead

    def get_resource(self) -> Resource:
        return self.__resource

    def perform_summoning_ritual(self, ritual: SummoningRitual):
        numUndead = sum(slot is not None for slot in self.__undead)
        if numUndead >= self.__max_controlled_undead:  # if too many undead
            print(
                f"I have too many undead! ({numUndead}/{self.__max_controlled_undead}) I can't take any more until one... re-perishes.")
            return
        if not ritual.can_be_performed_with_resources(self.__resource):
            print("I am too impoverished for such a demanding ritual! What do you expect me to do with only three small sticks and 4 cc of mouse blood")
            return

        ritual.consume_resources(self.__resource)
        id = self.__undead.index(None)
        self.__undead[id] = (ritual.create_undead(id))
        print(f"Rise, o evil {ritual.undead_type} and do my bidding!")
        return id

    def dismiss_undead(self, id):
        self.get_undead_from_id(id).__del__()
        self.__undead[id] = None

    def get_undead_from_id(self, id):
        # TODO : do this the hard way by checking IDs.
        return self.__undead[id]

    def level_up_undead(self, id):
        self.get_undead_from_id(id).increase_level()

    resource = property(get_resource)
