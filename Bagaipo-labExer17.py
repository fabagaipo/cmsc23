from abc import ABC,abstractmethod
from datetime import date,timedelta

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

class Printable(ABC):
    @abstractmethod
    def __str__(self) -> str:
        pass 

class Delivery(ABC):
    @abstractmethod
    def deliveryDetails(self) -> str:
        pass
    @abstractmethod
    def deliveryFee(self) -> float:
        pass
    @abstractmethod
    def estimatedDeliveryDate(self,processDate:date) -> float:
        pass
    @abstractmethod
    def changeDeliveryStatus(self,newStatus:str):
        pass


class Order:
    def __init__(self,productName:str, productPrice:float):
        self.__productName = productName
        self.__productPrice = productPrice
    def orderString(self) -> str:
        return "%s P %.2f" % (self.__productName,self.__productPrice)
    def price(self) -> float:
        return self.__productPrice

class StandardDelivery(Delivery):
    def __init__(self,location:str):
        self.__location = location
        self.__deliveryStatus = "Processing"
    def deliveryDetails(self) -> str:
        r = "STANDARD DELIVERY\nDELIVER TO:%s\nDELIVERY STATUS: %s\nDELIVERY FEE: P %.2f" % (self.__location,self.__deliveryStatus,self.deliveryFee())
        return r
    def deliveryFee(self) -> float:
        return 500
    def estimatedDeliveryDate(self,processDate:date) -> float:
        return processDate + timedelta(days = 7)
    def changeDeliveryStatus(self,newStatus:str):
        self.__deliveryStatus = newStatus

class Shipment:
    def __init__(self, orderList:[Order], processDate: date, location):
        self._orderList = orderList
        self._processDate = processDate
        self._delivery = self.delivery(location)

    def delivery(self,location:str) -> Delivery:
        return StandardDelivery(location)

    def totalPrice(self) -> str:
        t = 0.0
        for order in self._orderList:
            t+=order.price()
        return t

    def shipmentDetails(self) -> str:
        r = "ORDERS:" + str(self._processDate) + "\n"
        for order in self._orderList:
            r += order.orderString() + "\n"
        r += "\n"
        r += "TOTAL PRICE OF ORDERS: P "  + str(self.totalPrice()) + "\n"
        r += self._delivery.deliveryDetails() + "\n\n"
        r += "PRICE WITH DELIVERY FEE : P " + str(self.totalPrice()+self._delivery.deliveryFee()) + "\n"
        r += "ESTIMATED DELIVERY DATE: " + str(self._delivery.estimatedDeliveryDate(self._processDate)) + "\n"
        return r

class PrintableShipment(Printable):
    def __init__(self, shipment: Shipment) -> None:
        self._shipment = shipment

    def __str__(self) -> str:
        return self._shipment.shipmentDetails()

class ExpressDelivery(Delivery):
    def __init__(self,location:str):
        self.__location = location
        self.__deliveryStatus = "Processing"
    def deliveryDetails(self) -> str:
        r = "EXPRESS DELIVERY\nDELIVER TO:%s\nDELIVERY STATUS: %s\nDELIVERY FEE: P %.2f" % (self.__location,self.__deliveryStatus,self.deliveryFee())
        return r
    def deliveryFee(self) -> float:
        return 1000
    def estimatedDeliveryDate(self,processDate:date) -> float:
        return processDate + timedelta(days = 2)
    def changeDeliveryStatus(self,newStatus):
        self.__deliveryStatus = newStatus

class ExpressShipment(Shipment):
    def delivery(self,location) -> Delivery:
        return ExpressDelivery(location)

#Standard Delivery
o1 = [Order("Surface Pro 7",40000),Order("Zzzquil",900)]
s = Shipment(o1,date(2019,11,1),"Cebu City")
print(s.shipmentDetails())

#Express Delivery
o2 = [Order("Mac Pro",389990),Order("Pro Stand",58900)]
x: Shipment = ExpressShipment(o2,date(2019,11,1), "Cebu City")
y: Printable = PrintableShipment(x)
print(y)