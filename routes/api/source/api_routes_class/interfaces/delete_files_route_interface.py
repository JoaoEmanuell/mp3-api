from abc import ABC, abstractmethod

class DeleteFilesRouteInterface(ABC) :

    @abstractmethod
    def __init__(self, hash : str) -> None :
        raise NotImplementedError()

    @abstractmethod
    def delete_files(self) -> None :
        raise NotImplementedError()

    @abstractmethod
    def private__delete_json(self) -> None :
        raise NotImplementedError()

    @abstractmethod
    def private__delete_original_file(self) -> None :
        raise NotImplementedError()

    @abstractmethod
    def private__delete_converted_file(self) -> None :
        raise NotImplementedError()