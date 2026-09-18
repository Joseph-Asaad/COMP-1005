from abc import ABC


class Undead():

    def __init__(self, id, health, power):
        self._health = health
        self.__power = power
        self.__unit_identifier = None
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
        return self._health

    health = property(get_max_health, None)

    def get_power(self):
        return self.__power

    def increase_level(self):
        if self.__level >= self.MAX_LEVEL:
            return False
        self.__level += 1
        self._health += self.LEVEL_HEALTH_GAIN
        self.__power += self.LEVEL_POWER_GAIN
        print(self)
        return True

    power = property(get_power, None)

    def command(self):
        print("I will follow your command!")

    def __str__(self):
        return f"id={self.__unit_identifier}, name={self.__name}, health={self._health}/{self.MAX_HEALTH}, power={self.power}/{self.MAX_POWER}"
