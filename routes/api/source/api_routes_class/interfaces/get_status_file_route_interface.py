from abc import ABC, abstractmethod
from typing import Dict, Union, Type
from ...interfaces import ExtractLogInfosInterface


class GetStatusFileRouteInterface(ABC):
    @abstractmethod
    def __init__(
        self,
        path: str = None,
        hash: str = None,
        extract_log: Type[ExtractLogInfosInterface] = None,
    ) -> None:
        """Init

        Args:
            path (str): Path to status json files. Defaults to None.
            hash (str): Hash to json file, provided by upload route. Defaults to None.
            extract_log (Type[ExtractLogInfosInterface]):
                Extract log to ffmpeg log file

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

                'current' and 'total' they're used to calculate the progress of the conversion, and update a progress bar.
        """
        raise NotImplementedError()

    @abstractmethod
    def set_atributes(self, **kwargs) -> None:
        """
        Set atributes

        Args:
            **kwargs (dict): Dict of atributes
            attributes are defined in __init__

        """
        raise NotImplementedError()
