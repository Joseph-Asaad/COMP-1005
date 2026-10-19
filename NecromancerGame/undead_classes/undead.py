from abc import ABC


class Undead(ABC):
    """
    This class represents an undead creature.

    Attributes
    ----------

    health : int 
        Current number of health points - read only.

    power : int
        Current amount of power - read only.

    __name : str
        Name of this individual unit.

    __level : int
        Current level.

    MIN_HEALTH : int
        Lowest possible health for this unit.

    MAX_HEALTH : int
        Highest possible health, will not gain health beyond this value.

    MIN_POWER : int
        Lowest possible power (initial value).

    MAX_POWER : int
        Highest possible power, will not gain power beyond this value.

    MIN_LEVEL : int
        Initial level.

    MAX_LEVEL : int
        Highest attainable level for this undead.

    LEVEL_POWER_GAIN : int
        How much power the undead gains with each level-up.    

    LEVEL_HEALTH_GAIN : int
        How much health the undead gains with each level-up.

    Methods
    -------

    increase_level(void) : bool
        Increases the level of the Undead if possible, otherwise returns False.

    command(void) : void
        Prints an appropriate string on command.

    """

    def __init__(self, id, health, power):
        self.__health = health
        self.__power = power
        self.__name = None
        self.__level = 1
        self.id = id

        self.MIN_HEALTH = 0
        self.MAX_HEALTH = 100
        self.MIN_POWER = 1
        self.MAX_POWER = 100
        self.MIN_LEVEL = 1
        self.MAX_LEVEL = 100

        self.LEVEL_POWER_GAIN = 5
        self.LEVEL_HEALTH_GAIN = 1

    def get_max_health(self):
        return self.__health

    health = property(get_max_health, None)

    def get_power(self):
        return self.__power

    def increase_level(self):
        if self.__level >= self.MAX_LEVEL:
            return False
        self.__level += 1
        self.__health += self.LEVEL_HEALTH_GAIN
        self.__power += self.LEVEL_POWER_GAIN
        print(self)
        return True

    power = property(get_power, None)

    def command(self):
        print("I will follow your command!")

    def __str__(self):
        return f"id={self.id}, name={self.__name}, health={self.__health}/{self.MAX_HEALTH}, power={self.power}/{self.MAX_POWER}"
