from abc import ABC,abstractmethod

class SearchAlgorithm(ABC):
    def __init__(self, target:int, searchSpace:[int]):
        self._searchSpace = searchSpace
        self._currentIndex = 0
        self._solutions = []
        self._target = target

    def bruteForceSolution(self):
        candidate = self.first()
        while(self.isSearching()):
            if self.isValid(candidate):
                self.updateSolution(candidate)
            candidate = self.next()
        return self._solutions

    def first(self) -> int:
        return self._searchSpace[0]

    def next(self) -> int:
        self._currentIndex += 1
        if self.isSearching():
            return self._searchSpace[self._currentIndex]

    def isSearching(self) -> bool:
        return self._currentIndex < len(self._searchSpace)

    def __str__(self) -> str:
        return str(self._solutions)

    @abstractmethod
    def isValid(self, candidate) -> bool:
        pass

    @abstractmethod
    def updateSolution(self, candidate):
        pass


class EqualitySearchAlgorithm(SearchAlgorithm):
    def isValid(self, candidate):
        return candidate == self._target

    def updateSolution(self, candidate):
        return self._solutions.append(candidate)

class DivisibilitySearchAlgorithm(SearchAlgorithm):
    def isValid(self, candidate):
        return candidate % self._target == 0

    def updateSolution(self, candidate):
        return self._solutions.append(candidate)

class MinimumSearchAlgorithm(SearchAlgorithm):
    def __init__(self, searchSpace:[int]):
        super().__init__(searchSpace[0], searchSpace)

    def isValid(self, candidate):
        return candidate+1 < self._target

    def updateSolution(self, candidate):
        return self._solutions.append(candidate)

s = [2,3,1,0,6,2,4]
print(s)
#Equality Search target = 2
eq = EqualitySearchAlgorithm(2, s)
eq.bruteForceSolution()
print(eq)

#Divisibility Search target = 2
div = DivisibilitySearchAlgorithm(2, s)
div.bruteForceSolution()
print(div)

#Minimum search target = None/0
minim = MinimumSearchAlgorithm(s)
minim.bruteForceSolution()
print(minim)