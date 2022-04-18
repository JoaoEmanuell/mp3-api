from abc import ABC, abstractclassmethod

class ConversorInterface(ABC) :
    @abstractclassmethod
    def convert(cls, audio : str) -> None:
        raise NotImplementedError