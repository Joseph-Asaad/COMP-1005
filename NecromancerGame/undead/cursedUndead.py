from undead.undead import Undead


class CursedUndead(Undead):
    def command(self):
        super().command()
        print("I will curse your enemies?")

    def combat_style(self):
        return "cursing?"
