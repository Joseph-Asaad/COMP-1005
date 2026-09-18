from undead.undead import Undead
from undead.cursedUndead import CursedUndead
from undead.warriorUndead import WarriorUndead


class DeathKnight(CursedUndead, WarriorUndead):

    def __init__(self, id, initial_health, initial_power):
        Undead.__init__(self, id, initial_health, initial_power)

    def command(self):
        CursedUndead.command(self)
        WarriorUndead.command(self)

    def combat_style(self):
        return super().combat_style()

    def compare_combat_styles(self):
        return "Im sorry what do you mean by compare? You want an essay or something?"
