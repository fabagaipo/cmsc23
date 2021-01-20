from abc import ABC,abstractmethod

class Iterator(ABC):
    @abstractmethod
    def next(self):
        pass

    @abstractmethod
    def hasNext(self):
        pass

class Collection(ABC):
    @abstractmethod
    def newIterator(self):
        pass

class MyList(Collection):
    def __init__(self, elements):
        self.__elements = elements

    def size(self):
        return len(self.__elements)

    def elementAtIndex(self,index):
        return self.__elements[index]

    def newIterator(self):
        return ListIterator(self)

    def newReverseIterator(self):
        return ReverseListIterator(self)

class ListIterator(Iterator):
    def __init__(self, some_list: MyList):
        self.__traversedList = some_list
        self.__currentIndex = 0

    def next(self):
        self.__currentIndex += 1
        return self.__traversedList.elementAtIndex(self.__currentIndex-1)

    def hasNext(self):
        return self.__currentIndex < self.__traversedList.size()

class ReverseListIterator(Iterator):
    def __init__(self, some_list: MyList):
        self.__traversedList = some_list
        self.__currentIndex = some_list.size()

    def next(self):
        self.__currentIndex -= 1
        return self.__traversedList.elementAtIndex(self.__currentIndex)

    def hasNext(self):
        return self.__currentIndex > 0

c:Collection = MyList([1,2,3,4])
itera:Iterator = c.newIterator()
ritera:Iterator = c.newReverseIterator()

print("Iteration:")
while(itera.hasNext()):
    print(itera.next())

print("Reverse Iteration:")
while(ritera.hasNext()):
    print(ritera.next())