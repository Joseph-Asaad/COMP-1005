from undead.undead import Undead
from undead.cursedUndead import CursedUndead
from undead.warriorUndead import WarriorUndead


class DeathKnight(CursedUndead, WarriorUndead):

    def __init__(self, id, initial_health, initial_power):
        Undead.__init__(self, id, initial_health, initial_power)

        self.MIN_HEALTH = 40
        self.MAX_HEALTH = 1000
        self.MIN_POWER = 10
        self.MAX_POWER = 1000
        self.MIN_LEVEL = 10
        self.MAX_LEVEL = 1000

        self.LEVEL_POWER_GAIN = 50
        self.LEVEL_HEALTH_GAIN = 10

    def command(self):
        CursedUndead.command(self)
        WarriorUndead.command(self)

    def combat_style(self):
        return super().combat_style()

    def compare_combat_styles(self):
        CursedUndead.combat_style(self)
        WarriorUndead.combat_style(self)
