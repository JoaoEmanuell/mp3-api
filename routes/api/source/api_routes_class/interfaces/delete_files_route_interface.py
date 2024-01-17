from abc import ABC, abstractmethod
from typing import Dict


class DeleteFilesRouteInterface(ABC):
    """
    This class is an interface for the DeleteFilesRoute class.

    Args:
        ABC (_type_): _description_

    Raises:
        NotImplementedError : NotImplementedError
    """

    @abstractmethod
    def __init__(self, hash: str = None) -> None:
        """
        Initialize the class

        Args:
            hash (str): Hash provide by /upload/ route

        Raises:
            NotImplementedError: NotImplementedError
        """
        raise NotImplementedError()

    def set_atributes(self, **kwargs) -> None:
        """
        Set atributes

        Args:
            **kwargs (dict): Dict of atributes
            attributes are defined in __init__

        Raises:
            NotImplementedError: NotImplementedError
        """
        raise NotImplementedError()

    @abstractmethod
    def main(self) -> Dict[str, str]:
        """
        Delete files from the server.
        Claim the private functions : delete json, original file and converted files.

        Raises:
            NotImplementedError: NotImplementedError
        """
        raise NotImplementedError()

    @abstractmethod
    def private__delete_json(self) -> None:
        """
        Delete json file from the server.

        Raises:
            NotImplementedError: NotImplementedError
        """
        raise NotImplementedError()

    @abstractmethod
    def private__delete_original_file(self) -> None:
        """
        Delete original file from the server.

        Raises:
            NotImplementedError: NotImplementedError
        """
        raise NotImplementedError()

    @abstractmethod
    def private__delete_converted_file(self) -> None:
        """
        Delete converted file from the server.

        Raises:
            NotImplementedError: NotImplementedError
        """
        raise NotImplementedError()
