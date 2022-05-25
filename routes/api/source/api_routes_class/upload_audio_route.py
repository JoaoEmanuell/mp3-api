from flask import request
from werkzeug.utils import secure_filename
from werkzeug.datastructures import FileStorage
from threading import Thread
from typing import Tuple, Dict

from ..atributes_manage import AtributeClass
from .interfaces import UploadAudioRouteInterface
from ..interfaces import ConversorInterface, HashInterface

class UploadAudioRoute(UploadAudioRouteInterface) :

    def __init__(self, path: str = None, filename: str = None, file: request = None, conversor: ConversorInterface = None, hash : HashInterface = None) -> None:
        self.__path = path
        self.__filename = filename
        self.__file = file
        self.__conversor = conversor
        self.__hash = hash

    def set_atributes(self, **kwargs) -> None :

        keys : Tuple[Tuple[str, type]] = (
            ('path', str), 
            ('filename', str),
            ('file', request),
            ('conversor', ConversorInterface),
            ('hash', HashInterface),
        )

        for key_tuple in keys :

            if key_tuple[0] in kwargs :
                AtributeClass.setattr(self, f'__{key_tuple[0]}', kwargs[key_tuple[0]])
    
    def main(self) -> Dict[str, str] :

        file : FileStorage = self.__file.files["file"]
        hash = self.__hash.generate_random_hash()
        filename = f'{hash}{secure_filename(file.filename)}'

        if filename == '' :
            return {'message' : 'No file selected'}
        
        file.save(f'{self.__path}{filename}')

        self.private__start_conversion()

        return {'message' : 'File uploaded successfully', 'hash' : filename}

    def private__start_conversion(self) -> None :
        Thread(target=self.__conversor.convert, args=(f'{self.__path}{self.__filename}',)).start()