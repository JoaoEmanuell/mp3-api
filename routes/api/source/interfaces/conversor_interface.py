from abc import ABC, abstractmethod

class ConversorInterface(ABC) :
    @abstractmethod
    def convert(self, audio : str) -> None:
        raise NotImplementedError