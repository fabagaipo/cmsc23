from abc import ABC, abstractmethod

class Date:
    def __init__(self, month:int, day:int, year:int):
        self.__month = month
        self.__day = day
        self.__year = year
    def __eq__(self, otherDate):
        if self.__month == otherDate.__month and self.__day == otherDate.__day and self.__year == otherDate.__year:
            return True
        return False
    def __ne__(self, otherDate):
        return not self == otherDate
    def __lt__(self, otherDate):
        if self.__day < otherDate.__day and (self.__month <= otherDate.__month or self.__year <= otherDate.__year):
            return True
        elif  self.__month < otherDate.__month and (self.__day <= otherDate.__day or self.__year <= otherDate.__year):
            return True
        elif self.__year < otherDate.__year and (self.__day <= otherDate.__day or self.__month <= otherDate.__month):
            return True
        return False
    def __le__(self, otherDate):
        if self.__eq__(otherDate) or self.__lt__(otherDate):
            return True
        return False
    def __gt__(self, otherDate):
        if self.__day > otherDate.__day and (self.__month >= otherDate.__month or self.__year >= otherDate.__year):
            return True
        elif  self.__month > otherDate.__month and (self.__day >= otherDate.__day or self.__year >= otherDate.__year):
            return True
        elif self.__year > otherDate.__year and (self.__day >= otherDate.__day or self.__month >= otherDate.__month):
            return True
        return False
    def __ge__(self, otherDate):
        if self.__eq__(otherDate) or self.__gt__(otherDate):
            return True
        return False
    def __add__(self, number: int):
        self.__day += number
        if ((self.__year % 4 == 0 and self.__year % 100 != 0) or self.__year % 400 == 0) and self.__month == 2:
            modulo = 29
        elif self.__month == 2:
            modulo = 28
        elif self.__month not in [1, 3, 5, 7, 8, 10, 12]:
            modulo = 30
        else:
            modulo = 31
        while self.__day > modulo:
            self.__day -= modulo
            self.__month += 1
            while self.__month > 12:
                self.__year += 1
                self.__month -= 12
            if ((self.__year % 4 == 0 and self.__year % 100 != 0) or self.__year % 400 == 0) and self.__month == 2:
                modulo = 29
            elif self.__month == 2:
                modulo = 28
            elif self.__month not in [1, 3, 5, 7, 8, 10, 12]:
                modulo = 30
            else:
                modulo = 31
        return self
    def __sub__(self, number: int):        
        self.__day -= number
        while self.__day <= 0:
            if ((self.__year % 4 == 0 and self.__year % 100 != 0) or self.__year % 400 == 0) and self.__month == 2:
                modulo = 29
            elif self.__month == 2:
                modulo = 28
            elif self.__month not in [1, 3, 5, 7, 8, 10, 12]:
                modulo = 30
            else:
                modulo = 31
            self.__day += modulo
            self.__month -= 1
            while self.__month <= 0:
                self.__year -= 1
                self.__month += 12
        return self + 2
    def distance(self, otherDate) -> int:
        days = 0
        if self == otherDate:
            return days
        if self < otherDate:
            while self != otherDate:
                self += 1
                days += 1
            return days
        if self > otherDate:
            while self != otherDate:
                self -= 1
                days += 1
            return days
    def __str__(self) -> str:
        return "{}/{}/{}".format(self.__month, self.__day, self.__year)

class BorrowableItem(ABC):
    @abstractmethod
    def borrowableItemId(self)-> int:
        pass
    @abstractmethod
    def uniqueItemId(self) -> int:
        pass
    @abstractmethod
    def commonName(self) -> str:
        pass
    @abstractmethod
    def totalPenaltyDays(self) -> str:
        pass

class Page:
    def __init__(self, sectionHeader:str, body: str):
        self.__sectionHeader = sectionHeader
        self.__body = body

class Periodical(BorrowableItem):
    def __init__(self, periodicalID: int, title: str, issue: Date, pages: [Page]):
        self.__periodicalID = periodicalID
        self.__title = title
        self.__issue = issue
        self.__pages = pages
        self.__penaltyDays = 1
    def borrowableItemId(self) -> int:
        return self.__borrowableItemId
    def uniqueItemId(self) -> int:
        return self.__periodicalID
    def commonName(self) -> str:
        return "{}:{}".format(self.__title, self.__issue)
    def totalPenaltyDays(self) -> int:
        return self.__penaltyDays

class PC(BorrowableItem):
    def __init__(self, pcID: int):
        self.__pcID = pcID
        self.__penaltyDays = 0
    def borrowableItemId(self) -> int:
        return self.__borrowableItemId
    def uniqueItemId(self) -> int:
        return self.__pcID
    def commonName(self) -> str:
        return "PC{}".format(self.__pcID)
    def totalPenaltyDays(self) -> int:
        return self.__penaltyDays

class Book(BorrowableItem):
    def __init__(self, bookId:int, title:str, author:str, publishDate:Date, pages: [Page]):
        self.__bookId = bookId
        self.__title = title
        self.__publishDate = publishDate
        self.__author = author
        self.__pages = pages
        self.__penaltyDays = 7
    def borrowableItemId(self) -> int:
        return self.__borrowableItemId
    def coverInfo(self) -> str:
        return "\nTitle: {}\nAuthor: {}".format(self.__title, self.__author)
    def uniqueItemId(self) -> int:
        return self.__bookId
    def commonName(self) -> str:
        return "Borrowed Item: {} by {}".format(self.__title, self.__author)
    def totalPenaltyDays(self) -> int:
        return self.__penaltyDays

class LibraryCard:
    def __init__(self, idNumber: int, name: str, borrowedItems: {BorrowableItem: Date}):
        self.__idNumber = idNumber
        self.__name = name
        self.__borrowedItems = borrowedItems
    def borrowItem(self, item:BorrowableItem, date:Date):
        self.__borrowedItems[item] = date
    def borrowerReport(self) -> str:
        r:str = self.__name + "\n"
        for borrowedItem in self.__borrowedItems:
            r = r + borrowedItem.commonName() + ", borrow date: {}\n".format(self.__borrowedItems[borrowedItem].mdyFormat())
        return r
    def returnItem(self, b: BorrowableItem):
        self.__borrowedItems.pop(b)
    def itemsDue(self, today: Date) -> [BorrowableItem]:
        due_dates = {'0': 7, '1': 1, '2': 0}
        return [borrowedItem for borrowedItem in self.__borrowedItems.keys() if self.__borrowedItems[borrowedItem] + borrowedItem.totalPenaltyDays() >= today]
    def penalty(self, b: BorrowableItem, today: Date) -> float:
        return today.distance(self.__borrowedItems[b]) * 3.5 if today.distance(self.__borrowedItems[b]) <= b.totalPenaltyDays() else 14
    def totalPenalty(self, today: Date):
        total = 0
        for key, value in self.__borrowedItems.keys():
            total += self.penalty(key, today)
        return total
    def __str__(self):
        return "Name: {}\tBorrower's ID: {}\nItems in cart: {}".format(self.__name, self.__idNumber, [(borrowedItem.borrowableItemId(), self.__borrowedItems[borrowedItem].mdyFormat()) for borrowedItem in self.__borrowedItems.keys()])
