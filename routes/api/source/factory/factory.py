# Global imports

from typing import Type, Tuple
from abc import ABC

# Local imports

from ..interfaces import FactoryInterface
from ..hash import Hash
from ..conversor import Conversor

class Factory(FactoryInterface) :
    def __init__(self) -> None:
        self.__representatives : Tuple[ABC] = (
            Hash,
            Conversor
        )

    def get_representative(self, interface: Type[ABC], *args, **kwargs) -> ABC:
        for representative in self.__representatives :
            if isinstance(representative(*args, **kwargs), interface) :
                return representative(*args, **kwargs)
        raise ValueError(f'{interface} has no representative')

