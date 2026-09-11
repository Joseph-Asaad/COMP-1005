from resource import Resource
from summoning_ritual import SummoningRitual
import undead as undead
from necromancer import Necromancer

resource_pack_1 = Resource()

resource_pack_1.add_resource([999, 999, 999, 999, 999])
print(resource_pack_1.ectoplasm)

james = Necromancer("james", resource_pack_1, 5)


summonSkeletonWarrior = SummoningRitual(
    undead.SkeletonWarrior, "Summon Skeleton Warrior", "Skeleton Warrior", 20, 30, [1, 0, 4, 2, 2])

summonVengefulGhost = SummoningRitual(
    undead.VengefulGhost, "Summon Vengeful Ghost", "Vengeful Ghost", 90, 2, [0, 3, 0, 0, 8])

summonPutridZombie = SummoningRitual(
    undead.PutridZombie, "Summon Putrid Zombie", "Putrid Zombie", 90, 2, [0, 0, 4, 4, 2])

summonPhantomGuardian = SummoningRitual(
    undead.PhantomGuardian, "Summon Phantom Guardian", "Phantom Guardian", 90, 2, [0, 4, 0, 0, 5])


james.perform_summoning_ritual(summonPutridZombie)
james.perform_summoning_ritual(summonPhantomGuardian)
james.perform_summoning_ritual(summonSkeletonWarrior)
james.perform_summoning_ritual(summonVengefulGhost)
