from abc import ABC, abstractmethod
from typing import Dict, Type

class ExtractLogInfosInterface(ABC):
    """Extract data from ffmpeg conversion log"""

    @abstractmethod
    def __init__(self, log_path: str, error_class: Type[Exception]) -> None:
        """Init

        Args:
            log_path (str): Path to ffmpeg conversion log
            error_class (Type[Exception]): Error class to raise erros

        """        
        raise NotImplementedError()

    @abstractmethod
    def get_seconds(self) -> int:
        """Get seconds of the audio

        Returns:
            int: duration in seconds of the audio
        """
        raise NotImplementedError()

    @abstractmethod
    def get_bitrate(self) -> int:
        """Get bitrate

        Raises:
            ExtractLogInfosErrosInterface: 
                "Log Error!" case the bitrate not found.

        Returns:
            int: bitrate in kilobits per second.
        """
        raise NotImplementedError()

    @abstractmethod
    def get_current_file_size(self) -> Dict[str, int]:
        """Get current file size

        Raises:
            ExtractLogInfosErrosInterface: 
                "Conversion Error!" case conversion error.
                "Log Error!" case the log is invalid or not data.

        Returns:
            Dict[str, int]: {message: size}
        """        
        raise NotImplementedError()

    @abstractmethod
    def get_estimated_file_size(self) -> int:
        """Return the mp3 estimated file size

        Returns:
            int: size in kb
        """        
        raise NotImplementedError()

    @abstractmethod
    def get_filename(self) -> str:
        """Get filename

        Raises:
            ExtractLogInfosErrosInterface: 
                "Log Error!" case the filename not found.

        Returns:
            str: Filename from file
        """        
        raise NotImplementedError()