from abc import ABC, abstractmethod

class Sentence:
    def __init__(self, words: [str]):
        self.__words = words

    def __str__(self) -> str:
        sentenceString = ""
        for word in self.__words:
            sentenceString += word + " "
        return sentenceString[:-1]

class FormattedSentence(ABC, Sentence):
    def __init__(self, wrappedSentence):
        self._wrappedSentence = wrappedSentence

    @abstractmethod
    def __str__(self):
        pass

class BorderedSentence(FormattedSentence):
    def __str__(self) -> str:
        return "-" * (len(str(self._wrappedSentence)) + 2) + "\n|{}|\n".format(str(self._wrappedSentence)) +  "-" * (len(str(self._wrappedSentence)) + 2)

class FancySentence(FormattedSentence):
    def __str__(self) -> str:
        return "-+{}+-".format(self._wrappedSentence.__str__())

class UpperClassSentence(FormattedSentence):
    def __str__(self) -> str:
        return str(self._wrappedSentence).upper()

a = Sentence(["hey", "there"])
print(a)
b = BorderedSentence(a)
print(b)
c = FancySentence(a)
print(c)
d = UpperClassSentence(a)
print(d)
e = BorderedSentence(c)
print(e)
f = FancySentence(d)
print(f)