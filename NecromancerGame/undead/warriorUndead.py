from undead.undead import Undead


class WarriorUndead(Undead):

    def command(self):
        super().command()
        print("I will fight for you!")
