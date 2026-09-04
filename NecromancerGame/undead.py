class Undead:

    def __init__(self):
        self.__unit_identifier = None
        self.__name = None
        self.__health = None
        self.__level = None

        self.MIN_HEALTH = 0
        self.MAX_HEALTH = 100
        self.MIN_POWER = 1
        self.MAX_POWER = 100
        self.MIN_LEVEL = 1
        self.MAX_LEVEL = 100

        self.LEVEL_POWER_GAIN = 5
        self.LEVEL_HEALTH_GAIN = 1

    def get_max_health(self):
        return min(max(self.MIN_HEALTH, self.__level * self.LEVEL_HEALTH_GAIN), self.MAX_HEALTH)

    health = property(get_max_health, None)

    def get_power(self):
        return min(max(self.MIN_POWER, self.__level * self.LEVEL_POWER_GAIN), self.MAX_POWER)

    def increase_level(self):
        if self.__level > self.MAX_LEVEL:
            return False
        self.__level == min(
            # TODO: remove redundant check
            max(self.MIN_LEVEL, self.__level + 1, self.MAX_LEVEL))
        print(self)
        return True

    power = property(get_power, None)

    def __str__(self):
        return f"id={self.__unit_identifier}, name={self.__name}, health={self.__health}/{self.MAX_HEALTH}, power={self.power}/{self.MAX_POWER}"
