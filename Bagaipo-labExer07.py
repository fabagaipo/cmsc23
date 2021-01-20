from abc import ABC, abstractmethod
import time

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

class BankAccount(ABC):
    @abstractmethod
    def currentBal(self):
        pass

    @abstractmethod
    def displayAcc(self):
        pass

class Payroll(BankAccount):
    def __init__(self, accountNumber: int, pinNumber: int, name: str, birthdate: Date, address: str, contact: str, email : str, dateApplied: Date, balance: float):
        self.__accountType: str = "Payroll"
        self.__accountNumber = accountNumber
        self.__pinNumber = pinNumber
        self.__name = name
        self.__birthdate = birthdate
        self.__address = address
        self.__contact = contact
        self.__email = email
        self.__dateApplied = dateApplied
        self.__currentBalance = balance
        self.__isActive: bool = True

    def currentBal(self) -> float:
        return self.__currentBalance

    def receiveTransferredFunds(self, transferredFund: float):
        self.__currentBalance += transferredFund

    def withdrawCurrBal(self, withdrawalAmount: float, inputPin: int) -> float:
        if inputPin == self.__pinNumber:
            if withdrawalAmount <= self.__currentBalance:
                self.__currentBalance -= withdrawalAmount
                return withdrawalAmount
            else:
                raise "Failed to Withdraw. Insufficient Funds."
        else:
            raise "Invalid Pin."
    
    def displayAcc(self):
        print("Account Number: {}\tAccount Type: {}\tDate Applied: {}\n\tName: {}\tBirthdate: {}\tContact: {}\n\tAddress: {}\tEmail: {}\n\nCurrent Balance: {}\tIs active?: {}".format(self.__accountNumber, self.__accountType, self.__dateApplied, self.__name, self.__birthdate, self.__contact, self.__address, self.__email, self.__currentBalance, self.__isActive))

class Debit(BankAccount):
    def __init__(self, accountNumber: int, pinNumber: int, name: str, birthdate: Date, address: str, contact: str, email : str, dateApplied: Date, balance: float):
        self.__accountType: str = "Debit"
        self.__accountNumber = accountNumber
        self.__pinNumber = pinNumber
        self.__name = name
        self.__birthdate = birthdate
        self.__address = address
        self.__contact = contact
        self.__email = email
        self.__dateApplied = dateApplied
        self.__currentBalance = balance
        self.__maintainingBalance: float = 500.00
        self.__isActive: bool = True
        self.__dateDeactivated: Date = dateApplied

    def currentBal(self) -> float:
        return self.__currentBalance

    def monthlyCompoundInterest(self, currentDate: Date):
        if currentDate.__day == 20:
            self.__currentBalance += self.currentBalance * 0.25833

    def depositCurrBal(self, depositedAmount: float, currentDate: Date):
        if self.__dateApplied == self.__dateDeactivated:
            self.currentBalance += depositedAmount
        if currentDate >= self.__dateDeactivated + 1:
            raise "Invalid Account."

    def withdrawCurrBal(self, withdrawalAmount: float, inputPin: int) -> float:
        if inputPin == self.__pinNumber:
            if withdrawalAmount <= self.__currentBalance:
                self.__currentBalance -= withdrawalAmount
                return withdrawalAmount
            else:
                raise "Failed to Withdraw. Insufficient Funds."
        else:
            raise "Invalid PIN Error: Account is now locked. You may only withdraw after 24 hours."
    
    def monthlyCurrentBalanceCheck(self, currentDate: Date):
        if self.__currentBalance < self.__maintainingBalance and currentDate.__day == 20:
            self.__isActive = False
            self.__dateDeactivated = currentDate
            raise "Account has been deactivated due to lower than minimum maintaining balance."

    def displayAcc(self):
        print("Account Number: {}\tAccount Type: {}\tDate Applied: {}\n\tName: {}\tBirthdate: {}\tContact: {}\n\tAddress: {}\tEmail: {}\n\nCurrent Balance: {}\tMaintaining Balance\tIs active?: {}".format(self.__accountNumber, self.__accountType, self.__dateApplied, self.__name, self.__birthdate, self.__contact, self.__address, self.__email, self.__currentBalance, self.__maintainingBalance, self.__isActive))

class Credit(BankAccount):
    pass

class BankSystem:
    pass
