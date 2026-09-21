# pyright: ignore[reportAttributeAccessIssue]
from resourceHandler import Resource
from summoning_ritual import SummoningRitual
from necromancer import Necromancer

from undead.undead import Undead
from undead.cursedUndead import CursedUndead
from undead.warriorUndead import WarriorUndead

from undead.phantomGuardian import PhantomGuardian
from undead.vengefulGhost import VengefulGhost
from undead.putridZombie import PutridZombie
from undead.skeletonWarrior import SkeletonWarrior
from undead.deathKnight import DeathKnight


james = Necromancer("james", 5)
james.get_resource().add_resource((999, 999, 999, 999, 999))

print(f"We have {james.get_resource().ectoplasm} ectoplasm")

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

# test = SummoningRitual(
# no workey
#    "hello", "Summon Phantom Guardian", "Phantom Guardian", 90, 2, (0, 4, 0, 0, 5))

print("  ---  Summoning stuff  ---   ")
james.perform_summoning_ritual(summonPutridZombie)
james.perform_summoning_ritual(summonPhantomGuardian)
james.perform_summoning_ritual(summonSkeletonWarrior)
james.perform_summoning_ritual(summonVengefulGhost)
theLastOne = james.perform_summoning_ritual(summonVengefulGhost)
james.perform_summoning_ritual(summonVengefulGhost)  # oh no
james.dismiss_undead(theLastOne)
scawyMonster = james.perform_summoning_ritual(summonDeathKnight)

print(james.get_undead_from_id(scawyMonster).health)
james.get_undead_from_id(scawyMonster).increase_level()
print(james.get_undead_from_id(scawyMonster).health)

print(
    f"The Death Knight fights by {james.get_undead_from_id(scawyMonster).combat_style()}")

print(f"We have {james.get_resource().ectoplasm} ectoplasm")

print(f"I have screwed up: {not (isinstance(james.get_undead_from_id(scawyMonster), CursedUndead) and isinstance(james.get_undead_from_id(scawyMonster), WarriorUndead) and isinstance(james.get_undead_from_id(scawyMonster), Undead))}")
