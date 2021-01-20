from abc import ABC, abstractmethod

class Headline:
    def __init__(self, headline:str, details:str, source:str):
        self.__headline = headline
        self.__details = details
        self.__source = source

    def __str__(self) -> str:
        return "%s(%s)\n%s" % (self.__headline, self.__source, self.__details)

class Weather:
    def __init__(self, temp:float, humidity:float, outlook:str):
        self.__temp = temp
        self.__humidity = humidity
        self.__outlook = outlook

    def __str__(self) -> str:
        return "%s: %.1fC %.1f" % (self.__outlook, self.__temp, self.__humidity)

class Subscriber(ABC):
    @abstractmethod
    def update(self):
        pass

class EmailSubscriber(Subscriber):
    def __init__(self, emailAddress: str):
        self.__emailAddress = emailAddress
        self.__currentHeadline: Headline = None
        self.__currentWeather: Weather = None

    def update(self, newHeadline: Headline = None, newWeather: Weather = None):
        self.__currentHeadline = newHeadline
        self.__currentWeather = newWeather

    def __str__(self):
        return "{}: Received \n1.News Update : {} \n2.Weather Update : {} ".format(self.__emailAddress, str(self.__currentHeadline), str(self.__currentWeather))

class FileLogger(Subscriber):
    def __init__(self, filename: str = "log.in"):
        self.__filename = filename

    def update(self, newHeadline: Headline = None, newWeather: Weather = None):
        with open(self.__filename, 'a+') as logfile:
            logfile.write("\n New Headline {}\n{}\n".format(str(newHeadline), str(newWeather)))

class PushNotifier:
    def __init__(self, currentWeather: Weather, currentHeadline: Headline):
        self.__currentWeather = currentWeather
        self.__currentHeadline = currentHeadline
        self.__subscribers = []

    def changeHeadline(self, newHeadline: Headline):
        self.__currentHeadline = newHeadline
        self.notifySubscribers()

    def changeWeather(self, newWeather: Weather):
        self.__currentWeather = newWeather
        self.notifySubscribers()

    def subscribe(self, newSubscriber: Subscriber):
        self.__subscribers.append(newSubscriber)
        self.notifySubscribers()

    def unsubscribe(self, exSubscriber: Subscriber):
        self.__subscribers.remove(exSubscriber)

    def notifySubscribers(self):
        for sub in self.__subscribers:
            sub.update(self.__currentHeadline, self.__currentWeather)

h = Headline("Dalai Lama Triumphantly Names Successor After Discovering Woman With ‘The Purpose Of Our Lives Is To Be Happy’ Twitter Bio","Details","The Onion")
w = Weather(25.0,0.7,"Cloudy")
print(h)
print(w)
p = PushNotifier(w, h)
f = FileLogger("logs.in")
e = EmailSubscriber("fabagaipo@up.edu.ph")
p.subscribe(f)
p.subscribe(e)
print(e)
p.changeHeadline(Headline("Global Pop Superstars BTS join Smart Family","PH Armies going crazy", "ABS-CBN News"))
print(e)