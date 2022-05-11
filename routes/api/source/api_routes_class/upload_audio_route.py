from flask import request
from threading import Thread

from .interfaces import UploadAudioRouteInterface
from ..interfaces import ConversorInterface

class UploadAudioRoute(UploadAudioRouteInterface) :
    def set_atributes(self, **kwargs) -> None : 
        pass

    def save_file(self, path : str, filename : str, file : request) -> None :
        file.save(f'{path}{filename}')

    def start_conversion(self, conversor : ConversorInterface, path : str, filename : str) -> None :
        Thread(target=conversor.convert, args=(f'{path}{filename}',)).start()