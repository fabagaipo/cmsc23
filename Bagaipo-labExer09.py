from random import randint
from abc import ABC, abstractmethod

class Monster(ABC):
    @abstractmethod
    def announce(self):
        pass

    @abstractmethod
    def move(self):
        pass

class Bokoblin(Monster):
    def __init__(self, *args):
        self.__creatureType: str = str(args[0])
        self.__damageAmount: int = int(args[1])
        self.__weaponType: str = str(args[2])
        self.__armorType: str = str(args[3])
    def bludgeon(self):
        print("{} bludgeons you with a {} for {} damage".format(self.__creatureType, self.__weaponType, self.__creatureType))
    def defend(self):
        print("{} defends itself with a {}".format(self.__creatureType, self.__armorType))
    def announce(self):
        print("A {} appeared".format(self.__creatureType))
    def move(self):
        if randint(1,3) > 1:
            self.bludgeon()
        else:
            self.defend()

class NormalBokoblin(Bokoblin):
    def __init__(self):
        super().__init__("Bokoblin", 1, "boko club", "boko shield")
    
class BlueBokoblin(Bokoblin):
    def __init__(self):
        super().__init__("Blue Bokoblin", 2, "spiked boko club", "spiked boko shield")

class SilverBokoblin(Bokoblin):
    def __init__(self):
        super().__init__("Silver Bokoblin", 5, "dragonbone boko club", "dragonbone boko shield")

class Moblin(Monster):
    def __init__(self, *args):
        self.__creatureType: str = str(args[0])
        self.__damageAmount: [int] = [int(args[1]), int(args[2])]
        self.__weaponType: str = str(args[3])
    def stab(self):
        print("{} stabs you with a {} for {} damage".format(self.__creatureType, self.__weaponType, self.__damageAmount[0]))
    def kick(self):
        print("{} kicks you for {} damage".format(self.__creatureType, self.__damageAmount[1]))
    def announce(self):
        print("A {} appeared".format(self.__creatureType))
    def move(self):
        if randint(1,3) > 1:
            self.stab()
        else:
            self.kick()

class NormalMoblin(Moblin):
    def __init__(self):
        super().__init__("Moblin", 3, 1, "spear")

class BlueMoblin(Moblin):
    def __init__(self):
        super().__init__("Blue Moblin", 5, 2, "rusty halberd")

class SilverMoblin(Moblin):
    def __init__(self):
        super().__init__("Silver Moblin", 10, 3, "knight's halberd")

class Lizalflos(Monster):
    def __init__(self, *args):
        self.__creatureType: str = str(args[0])
        self.__damageAmount: int = int(args[1])
        self.__weaponType: str = str(args[2])
    def throwBoomerang(self):
        print("{} throws its {} at you for {} damage".format(self.__creatureType, self.__weaponType, self.__damageAmount))
    def hide(self):
        print("{} camouflages itself".format(self.__creatureType))
    def announce(self):
        print("A {} appeared".format(self.__creatureType))
    def move(self):
        if randint(1,3) > 1:
            self.throwBoomerang()
        else:
            self.hide()

class NormalLizalflos(Lizalflos):
    def __init__(self):
        super().__init__("Lizalflos", 2, "lizal boomerang")

class BlueLizalflos(Lizalflos):
    def __init__(self):
        super().__init__("Blue Lizalflos", 3, "forked boomerang")

class SilverLizalflos(Lizalflos):
    def __init__(self):
        super().__init__("Silver Lizalflos", 7, "tri-boomerang")

class Dungeon(ABC):
    @abstractmethod
    def newBokoblin(self) -> Bokoblin:
        pass

    @abstractmethod
    def newMoblin(self) -> Moblin:
        pass

    @abstractmethod
    def newLizalflos(self) -> Lizalflos:
        pass

class EasyDungeon(Dungeon):
    def newBokoblin(self) -> Bokoblin:
        return NormalBokoblin()

    def newMoblin(self) -> Moblin:
        return NormalMoblin()

    def newLizalflos(self) -> Lizalflos:
        return NormalLizalflos()

class MediumDungeon(Dungeon):
    def newBokoblin(self) -> Bokoblin:
        return BlueBokoblin()

    def newMoblin(self) -> Moblin:
        return BlueMoblin()

    def newLizalflos(self) -> Lizalflos:
        return BlueLizalflos()

class HardDungeon(Dungeon):
    def newBokoblin(self) -> Bokoblin:
        return SilverBokoblin()

    def newMoblin(self) -> Moblin:
        return SilverMoblin()

    def newLizalflos(self) -> Lizalflos:
        return SilverLizalflos()

class Encounter:
    def __init__(self):
        self.__dungeon: Dungeon = [EasyDungeon() if RNG == 1 else MediumDungeon() if RNG == 2 else HardDungeon() for RNG in [randint(1, 3)]][0]
        self.__enemies: [Monster] = [self.__dungeon.newBokoblin() if RNG == 1 else self.__dungeon.newMoblin() if RNG == 2 else self.__dungeon.newLizalflos() for RNG in [randint(1,3) for RNG in range(randint(0, 8))]]

    def announceEnemies(self):
        print("%d monsters appeared" % len(self.__enemies))
        for enemy in self.__enemies:
            enemy.announce()

    def moveEnemies(self):
        for enemy in self.__enemies:
            enemy.move()

encounter = Encounter()
encounter.announceEnemies()
print()
encounter.moveEnemies()
