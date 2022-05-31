from abc import ABC, abstractmethod
from typing import Dict

class GetConvertedAudioRouteInterface(ABC):
    @abstractmethod
    def __init__(self, filename : str, url_base : str):
        raise NotImplementedError()

    @abstractmethod
    def main(self) -> Dict[str, str] :
        raise NotImplementedError()