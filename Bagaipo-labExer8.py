from abc import ABC, abstractmethod
from datetime import date,timedelta

class Delivery(ABC):
    @abstractmethod
    def estimatedTimeArrival(self) -> date:
        pass

    @abstractmethod
    def deliveryFee(self) -> float:
        pass
    
    @abstractmethod
    def deliveryDetails(self) -> str:
        pass
    
    @abstractmethod
    def changeDeliveryStatus(self):
        pass

class ExpressDelivery(Delivery):
    def __init__(self, location:str):
        self.__location = location
        self.__deliveryStatus = "Processing"
    def deliveryDetails(self) -> str:
        r = "EXPRESS DELIVERY\nDELIVER TO:%s\nDELIVERY STATUS: %s\nDELIVERY FEE: P%.2f" % (self.__location,self.__deliveryStatus,self.deliveryFee())
        return r
    def deliveryFee(self) -> float:
        return 1000
    def estimatedTimeArrival(self, processDate:date) -> float:
        return processDate + timedelta(days = 1)
    def changeDeliveryStatus(self,newStatus:str):
        self.__deliveryStatus = newStatus    

class Order:
    def __init__(self,productName:str, productPrice:float):
        self.__productName = productName
        self.__productPrice = productPrice
    def orderString(self) -> str:
        return "%s P%.2f" % (self.__productName,self.__productPrice)
    def price(self) -> float:
        return self.__productPrice

class StandardDelivery(Delivery):
    def __init__(self,location:str):
        self.__location = location
        self.__deliveryStatus = "Processing"
    def deliveryDetails(self) -> str:
        r = "STANDARD DELIVERY\nDELIVER TO: %s\nDELIVERY STATUS: %s\nDELIVERY FEE: P%.2f" % (self.__location,self.__deliveryStatus,self.deliveryFee())
        return r
    def deliveryFee(self) -> float:
        return 500
    def estimatedTimeArrival(self,processDate:date) -> float:
        return processDate + timedelta(days = 7)
    def changeDeliveryStatus(self,newStatus:str):
        self.__deliveryStatus = newStatus

class Shipment:
    def __init__(self, orderList:[Order], processDate: date, location: str):
        self._orderList = orderList
        self._processDate = processDate
        self._delivery = self.newDelivery(location)

    def newDelivery(self, location: str) -> Delivery:
        return StandardDelivery(location)

    def totalPrice(self) -> str:
        t = 0.0
        for order in self._orderList:
            t+=order.price()
        return t

    def shipmentDetails(self) -> str:
        r = "ORDERS :" + str(self._processDate) + "\n"
        for order in self._orderList:
            r += order.orderString() + "\n"
        r += "\n"
        r += "TOTAL PRICE OF ORDERS : P"  + str(self.totalPrice()) + "\n"
        r += self._delivery.deliveryDetails() + "\n\n"
        r += "PRICE WITH DELIVERY FEE : P" + str(self.totalPrice()+self._delivery.deliveryFee()) + "\n"
        r += "ESTIMATED DELIVERY DATE : " + str(self._delivery.estimatedTimeArrival(self._processDate))
        return r

class ExpressShipment(Shipment):
    def newDelivery(self, location) -> Delivery:
        return ExpressDelivery(location)

o = [Order("Surface Pro 7",40000),Order("Zzzquil",900)]
s = Shipment(o,date(2019,11,1),"Cebu City")
print(s.shipmentDetails())
