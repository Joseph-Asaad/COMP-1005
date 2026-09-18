from undead.undead import Undead
from undead.cursedUndead import CursedUndead
from undead.warriorUndead import WarriorUndead


class DeathKnight(CursedUndead, WarriorUndead):

    def __init__(self, id):
        Undead.__init__(self, id, 60, 50)

    def command(self):
        CursedUndead.command(self)
        WarriorUndead.command(self)
