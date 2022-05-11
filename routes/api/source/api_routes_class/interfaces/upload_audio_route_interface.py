from abc import ABC, abstractclassmethod
from flask import request

from ....source.interfaces import ConversorInterface

class UploadAudioRouteInterface(ABC) :
    """UploadAudioRouteInterface

    Args:
        ABC (_type_): _description_

    Raises:
        NotImplementedError: NotImplementedError
    """    

    @abstractclassmethod
    def set_atributes(self, **kwargs) -> None :
        """set_atributes

        Raises:
            NotImplementedError: NotImplementedError
        """
        raise NotImplementedError()

    @abstractclassmethod
    def save_file(self, path : str, filename : str, file : request) -> None :
        """save_file

        Args:
            path (str): Path to save file
            filename (str): Name of file
            file (request): File to save

        Raises:
            NotImplementedError: NotImplementedError
        """        
        raise NotImplementedError()

    @abstractclassmethod
    def start_conversion(self, conversor : ConversorInterface, path : str, filename : str) -> None :
        """start_conversion

        Args:
            conversor (ConversorInterface): ConversorInterface
            path (str): Path to file

        Raises:
            NotImplementedError: NotImplementedError
        """        
        raise NotImplementedError()