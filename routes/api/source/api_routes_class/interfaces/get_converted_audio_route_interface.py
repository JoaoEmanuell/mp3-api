from abc import ABC, abstractmethod
from typing import Dict

class GetConvertedAudioRouteInterface(ABC):
    @abstractmethod
    def __init__(self, filename : str = None, url_base : str = None):
        """Init

        Args:
            filename (str): Filename provide by route get parameter.
            url_base (str): Url base provide by route, use request to access it.

        """        
        raise NotImplementedError()

    @abstractmethod
    def main(self) -> Dict[str, str] :
        """Main class

        Raises:
            NotImplementedError: _description_

        Returns:
            Dict[str, str]: Dict with two keys, 
                audio : path to audio converted. 
                filename : name of audio converted.
        """        
        raise NotImplementedError()

    @abstractmethod
    def set_atributes(self, **kwargs) :
        """
        Set atributes

        Args:
            **kwargs (dict): Dict of atributes
            attributes are defined in __init__

        Raises:
            NotImplementedError: NotImplementedError
        """       
        raise NotImplementedError()