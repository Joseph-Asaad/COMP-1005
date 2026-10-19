class Necromancer:
    """

    This class represents a Necromancer.

    Attributes
    ----------
    __resource : Resource
        Resource object associated with the Necromancer.

    __max_controlled_undead : int
        The maximum number of undead the Necromancer can control.

    __undead : Undead[__max_controlled_undead]
        Array of Undead, corresponds to the currently controlled Undead.

    Methods
    -------
    get_resource(void) : Resource
        Returns associated Resource object.

    perform_summoning_ritual(ritual : SummoningRitual) : void
        Uses [ritual] to summon undead if possible, adds them to the Necromancer.

    dismiss_undead(id : int) : void
        Deletes the Undead with the ID [id], frees a space for another Undead to take its place.

    get_undead_from_id(id : int) : Undead
        Returns the Undead with the ID [id].

    level_up_undead(id : int) : void
        Levels up the Undead with the ID [id] by one level.

    """

    from resource_handler import Resource
    from summoning_ritual import SummoningRitual
    from undead_classes.undead import Undead

    def __init__(self, name: str, max_controlled_undead: int):
        # pyright: ignore[reportAttributeAccessIssue]
        from resource_handler import Resource
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
        print(
            f"Rise, o evil {ritual.undead_type.__name__} and do my bidding!")
        return id

    def dismiss_undead(self, id):
        undead = self.get_undead_from_id(id)
        print(
            f"Begone, o worthless {type(undead).__name__}! You are of no use to me!")
        del undead
        self.__undead[id] = None

    def get_undead_from_id(self, id) -> Undead:
        return next(undead for undead in self.__undead if undead.id == id)

    def level_up_undead(self, id):
        self.get_undead_from_id(id).increase_level()

    resource = property(get_resource)
