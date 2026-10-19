from undead_classes.undead import Undead


class WarriorUndead(Undead):

    def command(self):
        super().command()
        print("I will fight for you!")

    def combat_style(self):
        return "stabbin'"
