from .interfaces import DeleteFilesRouteInterface
from ..atributes_manage import AtributeClass

from pathlib import Path
from os import remove
from typing import Tuple

class DeleteFilesRoute(DeleteFilesRouteInterface) :
    def __init__(self, hash: str = None) -> None :
        self.__hash = hash
        self.__path = Path().absolute()

    def set_atributes(self, *args, **kwargs) -> None :

        keys : Tuple[str, type] = (
            ('hash', str), 
        )

        for key_tuple in keys :

            if key_tuple[0] in kwargs :
                AtributeClass.setattr(self, f'__{key_tuple[0]}', kwargs[key_tuple[0]])

    def delete_files(self) -> None:
        self.private__delete_converted_file()
        self.private__delete_json()
        self.private__delete_original_file()

    def private__delete_converted_file(self) -> None :
        try :
            remove(f'{self.__path}/static/{self.__hash}.mp3')
        except FileNotFoundError :
            return None

    def private__delete_json(self) -> None:
        try :
            remove(f'{self.__path}/status/{self.__hash}.json')
        except FileNotFoundError :
            return None

    def private__delete_original_file(self) -> None:
        try :
            remove(f'{self.__path}/audios/{self.__hash}.mp3')
        except FileNotFoundError :
            return None