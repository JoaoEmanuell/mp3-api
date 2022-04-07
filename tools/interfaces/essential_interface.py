from abc import ABC, abstractmethod
from typing import List

class EssentialInterface(ABC) :

    @abstractmethod
    def create_dirs(self, dirs : List[str]):
        raise NotImplementedError

    @abstractmethod
    def delete_old_files(self, dirs : List[str]):
        raise NotImplementedError