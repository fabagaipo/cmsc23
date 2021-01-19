from abc import ABC, abstractmethod

class Fraction:
    def __init__(self,num:int,denom:int):
        self.__num = num
        self.__denom = denom
    def num(self):
        return self.__num
    def denom(self):
        return self.__denom
    def __str__(self) -> str:
        return str(self.__num) + "/" + str(self.__denom)

class Operation(ABC):
    @abstractmethod
    def execute(self) -> Fraction:
        pass

    @abstractmethod
    def __str__(self):
        pass

class Addition(Operation):
    def execute(self, left: Fraction, right: Fraction):
        if left.denom() == right.denom():
            num = left.num() + right.num()
            return Fraction(num, left.denom() if num != 0 else 1)
        else:
            gcd = 0
            if left.denom() % right.denom() == 0 or right.denom() % left.denom() == 0:
                gcd = left.denom() if left.denom() > right.denom() else right.denom()
            else:
                gcd = left.denom() * right.denom()
            num = (gcd // left.denom()) * left.num() + (gcd // right.denom()) * right.num()
            return Fraction(num, gcd if num != 0 else 1)
    
    def __str__(self) -> str:
        return "+"

class Subtraction(Operation):
    def execute(self, left: Fraction, right: Fraction):
        if left.denom() == right.denom():
            num = left.num() - right.num()
            return Fraction(num, left.denom() if num != 0 else 1)
        else:
            gcd = 0
            if left.denom() % right.denom() == 0 or right.denom() % left.denom() == 0:
                gcd = left.denom() if left.denom() > right.denom() else right.denom()
            else:
                gcd = left.denom() * right.denom()
            num = (gcd // left.denom()) * left.num() - (gcd // right.denom()) * right.num()
            return Fraction(num, gcd if num != 0 else 1)
    
    def __str__(self) -> str:
        return "-"

class Multiplication(Operation):
    def execute(self, left: Fraction, right: Fraction):
        num, denom = left.num()*right.num(), left.denom()*right.denom()
        if num % denom == 0 or denom % num == 0:
            new_num = num // denom if num > denom else num // num
            denom = denom // num if denom > num else denom // denom
            num = new_num
        return Fraction(num, denom)
    
    def __str__(self) -> str:
        return "×"

class Division(Operation):
    def execute(self, left: Fraction, right: Fraction):
        num, denom = left.num()*right.denom(), left.denom()*right.num()
        if num % denom == 0 or denom % num == 0:
            new_num = num // denom if num > denom else num // num
            denom = denom // num if denom > num else denom // denom
            num = new_num
        return Fraction(num, denom)
    
    def __str__(self) -> str:
        return "÷"

class Calculation:
    def __init__(self, left:Fraction, right:Fraction, operation:Operation): #will cause an error when ran since Operation does not exist yet
        self.__left = left
        self.__right = right
        self.__operation = operation #the parameter that represents the operation
        self.__answer = operation.execute(left, right) #the answer should be calculated here

    def __str__(self):
        return str(self.__left) + " " + str(self.__operation) + " " + str(self.__right) + " = " + str(self.__answer)

f:Fraction = Fraction(1,4)
print(f)

add: Calculation = Calculation(f, f, Addition())
print(add)
subtract: Calculation = Calculation(f, f, Subtraction())
print(subtract)
multiply: Calculation = Calculation(f, f, Multiplication())
print(multiply)
divide: Calculation = Calculation(f, f, Division())
print(divide)
