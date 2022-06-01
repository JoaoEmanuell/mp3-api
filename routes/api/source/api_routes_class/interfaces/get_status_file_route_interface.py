from abc import ABC, abstractmethod
from typing import Dict, Union

class GetStatusFileRouteInterface(ABC):
    @abstractmethod
    def __init__(
        self,
        path : str = None,
        hash : str = None,
        ) -> None:
        """Init

        Args:
            path (str): Path to status json files. Defaults to None.
            hash (str): Hash to json file, provided by upload route. Defaults to None.

        """        
        raise NotImplementedError()

    @abstractmethod
    def main(self) -> Dict[str, Union[str, bool]]:
        """Main method

        Returns:
            Dict[str, str]: 
                The dict necessarily contain the key 'status' with the value 'True' or 'False'.
                Others keys :
                    'filename' : The filename of the converted audio.
                    'current' : The current status of the conversion.
                    'total' : The total of the conversion.
                
                current and total they're used to calculate the progress of the conversion, and update a progress bar.
        """        
        raise NotImplementedError()

    @abstractmethod
    def set_atributes(**kwargs) -> None:
        """
        Set atributes

        Args:
            **kwargs (dict): Dict of atributes
            attributes are defined in __init__

        """     
        raise NotImplementedError()