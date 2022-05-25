from abc import ABC, abstractmethod
from flask import request
from typing import Dict

from ....source.interfaces import ConversorInterface

class UploadAudioRouteInterface(ABC) :
    """UploadAudioRouteInterface

    Args:
        ABC (_type_): _description_

    Raises:
        NotImplementedError: NotImplementedError
    """    
    def __init__(self, 
                path : str = None, 
                filename : str = None, 
                file : request = None, 
                conversor : ConversorInterface = None
                ) -> None:
        """Init

        Args:
            path (str, optional): Path to save file. Defaults to None.
            filename (str, optional): Filename. Defaults to None.
            file (request, optional): File. Defaults to None.
            conversor (ConversorInterface, optional): Conversor class, subclass of ConversorInterface. Defaults to None.

        Raises:
            NotImplementedError: _description_
        """
        raise NotImplementedError()

    @abstractmethod
    def set_atributes(self, **kwargs) -> None :
        """set_atributes

        Raises:
            NotImplementedError: NotImplementedError
        """
        raise NotImplementedError()

    @abstractmethod
    def main(self) -> Dict[str, str] :
        """main method

        Raises:
            NotImplementedError: NotImplementedError
        """
        raise NotImplementedError()

    @abstractmethod
    def private__start_conversion(self, conversor : ConversorInterface, path : str, filename : str) -> None :
        """start_conversion

        Args:
            conversor (ConversorInterface): ConversorInterface
            path (str): Path to file

        Raises:
            NotImplementedError: NotImplementedError
        """        
        raise NotImplementedError()