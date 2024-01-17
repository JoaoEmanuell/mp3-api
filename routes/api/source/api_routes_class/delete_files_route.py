from .interfaces import DeleteFilesRouteInterface
from ..atributes_manage import AtributeClass

from pathlib import Path
from os import remove
from typing import Dict, Tuple


class DeleteFilesRoute(DeleteFilesRouteInterface):
    def __init__(self, hash: str = None) -> None:
        self.__hash = hash
        self.__path = Path().absolute()

    def set_atributes(self, **kwargs) -> None:
        keys: Tuple[Tuple[str, type]] = (("hash", str),)

        for key_tuple in keys:
            if key_tuple[0] in kwargs:
                AtributeClass.setattr(self, f"__{key_tuple[0]}", kwargs[key_tuple[0]])

    def main(self) -> Dict[str, str]:
        self.__hash = self.__hash.replace(".mp3", "")
        self.private__delete_converted_file()
        self.private__delete_json()
        self.private__delete_original_file()
        return {"message": "Files deleted successfully"}

    def private__delete_converted_file(self) -> None:
        try:
            remove(f"{self.__path}/static/{self.__hash}.mp3")
        except FileNotFoundError:
            return None

    def private__delete_json(self) -> None:
        try:
            remove(f"{self.__path}/status/{self.__hash}.txt")
        except FileNotFoundError:
            return None

    def private__delete_original_file(self) -> None:
        try:
            remove(f"{self.__path}/audios/{self.__hash}.mp3")
        except FileNotFoundError:
            return None
