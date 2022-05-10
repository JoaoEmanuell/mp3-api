from flask import request

from .interfaces import UploadAudioRouteInterface
from source.interfaces import ConversorInterface
from threading import Thread

class UploadAudioRoute(UploadAudioRouteInterface) :
    def set_atributes(cls, **kwargs) -> None : 
        pass

    def save_file(cls, path : str, filename : str, file : request) -> None :
        file.save(f'{path}{filename}')

    def start_conversion(cls, conversor : ConversorInterface, path : str, filename : str) -> None :
        Thread(target=conversor.convert, args=(f'{path}{filename}',)).start()