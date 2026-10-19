from resource_handler import Resource
from summoning_ritual import SummoningRitual
from necromancer import Necromancer

from undead_classes.undead import Undead
from undead_classes.cursed_undead import CursedUndead
from undead_classes.warrior_undead import WarriorUndead

from undead_classes.phantom_guardian import PhantomGuardian
from undead_classes.vengeful_ghost import VengefulGhost
from undead_classes.putrid_zombie import PutridZombie
from undead_classes.skeleton_warrior import SkeletonWarrior
from undead_classes.death_knight import DeathKnight

# Create a necromancer.
james = Necromancer("james", 5)
# Give him some resources.
james.get_resource().add_resource((99, 99, 99, 99, 99))

# Show the amount of an arbitrary resource.
print(f"We have {james.get_resource().ectoplasm} ectoplasm")

# Create a variety of summoning rituals.
summonSkeletonWarrior = SummoningRitual(
    SkeletonWarrior, "Summon Skeleton Warrior", "Skeleton Warrior", 20, 30, (1, 0, 4, 2, 2))

summonVengefulGhost = SummoningRitual(
    VengefulGhost, "Summon Vengeful Ghost", "Vengeful Ghost", 90, 2, (0, 3, 0, 0, 8))

summonPutridZombie = SummoningRitual(
    PutridZombie, "Summon Putrid Zombie", "Putrid Zombie", 90, 2, (0, 0, 4, 4, 2))

summonPhantomGuardian = SummoningRitual(
    PhantomGuardian, "Summon Phantom Guardian", "Phantom Guardian", 90, 2, (0, 4, 0, 0, 5))

summonDeathKnight = SummoningRitual(
    DeathKnight, "Summon Death Knight", "Death Knight", 90, 2, (10, 20, 30, 40, 50))


try:
    test = SummoningRitual("a string", "Summon Phantom Guardian",
                           "Phantom Guardian", 90, 2, (0, 4, 0, 0, 5))
except:
    print("Doesn't work, \"a string\" is not a valid type.")


print("  ---  Summoning stuff  ---   ")  # Summon various creatures.
james.perform_summoning_ritual(summonPutridZombie)
james.perform_summoning_ritual(summonPhantomGuardian)
james.perform_summoning_ritual(summonSkeletonWarrior)
james.perform_summoning_ritual(summonVengefulGhost)
theLastOne = james.perform_summoning_ritual(summonVengefulGhost)

# Does not work, too many undead.
scawyMonster = james.perform_summoning_ritual(summonDeathKnight)
james.dismiss_undead(theLastOne)  # Dismiss an undead to create space.

scawyMonster = james.perform_summoning_ritual(
    summonDeathKnight)  # Now it works.

# Demonstrate that health and power increase with level.
print(james.get_undead_from_id(scawyMonster).health)
print(james.get_undead_from_id(scawyMonster).power)
james.get_undead_from_id(scawyMonster).increase_level()
print(james.get_undead_from_id(scawyMonster).health)
print(james.get_undead_from_id(scawyMonster).power)


# Print miscellaneous information.
print(
    f"The Death Knight fights by {james.get_undead_from_id(scawyMonster).combat_style()}")

print(f"We have {james.get_resource().ectoplasm} ectoplasm")

print(f"I have screwed up: {not (isinstance(james.get_undead_from_id(scawyMonster), CursedUndead) and isinstance(james.get_undead_from_id(scawyMonster), WarriorUndead) and isinstance(james.get_undead_from_id(scawyMonster), Undead))}")
