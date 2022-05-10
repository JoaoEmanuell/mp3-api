from abc import ABC, abstractmethod
from flask import request

from ....source.interfaces import ConversorInterface

class UploadAudioRouteInterface(ABC) :
    """UploadAudioRouteInterface

    Args:
        ABC (_type_): _description_

    Raises:
        NotImplementedError: NotImplementedError
    """    

    @abstractmethod
    def save_file(path : str, filename : str, file : request) -> None :
        """save_file

        Args:
            path (str): Path to save file
            filename (str): Name of file
            file (request): File to save

        Raises:
            NotImplementedError: NotImplementedError
        """        
        raise NotImplementedError()

    @abstractmethod
    def start_conversion(conversor : ConversorInterface, path : str) -> None :
        """start_conversion

        Args:
            conversor (ConversorInterface): ConversorInterface
            path (str): Path to file

        Raises:
            NotImplementedError: NotImplementedError
        """        
        raise NotImplementedError()