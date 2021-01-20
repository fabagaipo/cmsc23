from abc import ABC, abstractmethod

class Matter:
    def __init__(self, name:str):
        self.__name = name
        self.__state = SolidState(self) #change this to the appropriate initial state (liquid)
    def changeState(self, state):
        self.__state = state(self)
    def compress(self):
        self.__state.compress()
    def release(self):
        self.__state.release()
    def cool(self):
        self.__state.cool()
    def heat(self):
        self.__state.heat()
    def __str__(self):
        return "%s is currently a %s" % (self.__name, self.__state) #formatting strings just like you format strings in C

class State(ABC):
    @abstractmethod
    def compress(self):
        pass
    @abstractmethod
    def release(self):
        pass
    @abstractmethod
    def heat(self):
        pass
    @abstractmethod
    def cool(self):
        pass

class SolidState(State):
    def __init__(self, matter: Matter):
        self.__matter = matter
    def compress(self):
        pass
    def release(self):
        self.__matter.changeState(LiquidState)
    def heat(self):
        self.__matter.changeState(LiquidState)
    def cool(self):
        pass
    def __str__(self):
        return "solid"

class LiquidState(State):
    def __init__(self, matter: Matter):
        self.__matter = matter
    def compress(self):
        self.__matter.changeState(SolidState)
    def release(self):
        self.__matter.changeState(GasState)
    def heat(self):
        self.__matter.changeState(GasState)
    def cool(self):
        self.__matter.changeState(SolidState)
    def __str__(self):
        return "liquid"

class GasState(State):
    def __init__(self, matter: Matter):
        self.__matter = matter
    def compress(self):
        self.__matter.changeState(LiquidState)
    def release(self):
        pass
    def heat(self):
        pass
    def cool(self):
        self.__matter.changeState(LiquidState)
    def __str__(self):
        return "gas"

Ice = Matter("Ice")
Ice.compress()
print(Ice)
Ice.cool()
print(Ice)
Ice.heat()
print(Ice)
