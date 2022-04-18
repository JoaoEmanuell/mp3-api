from abc import ABC, abstractmethod
from typing import Type

class FactoryInterface(ABC) :
    @abstractmethod
    def __init__(self) -> None :
        raise NotImplementedError

    def get_representative(self, interface : Type[ABC]) -> ABC :
        raise NotImplementedError