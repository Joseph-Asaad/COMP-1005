

from undead_classes.cursed_undead import CursedUndead


class VengefulGhost(CursedUndead):
    def __init__(self, id, health, power):
        super().__init__(id, health, power)

        self.MIN_HEALTH = 0
        self.MAX_HEALTH = 100
        self.MIN_POWER = 1
        self.MAX_POWER = 100
        self.MIN_LEVEL = 1
        self.MAX_LEVEL = 100

        self.LEVEL_POWER_GAIN = 5
        self.LEVEL_HEALTH_GAIN = 1
