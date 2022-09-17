from typing import Tuple, Dict, Union, Type
from json import loads
from os.path import join

from .interfaces import GetStatusFileRouteInterface
from ..interfaces import ExtractLogInfosInterface
from ..conversor.ffmpeg import ExtractLogInfosError
from ..atributes_manage import AtributeClass

class GetStatusFileRoute(GetStatusFileRouteInterface) :
    def __init__(
        self, 
        path: str = None, 
        hash: str = None,
        extract_log: Type[ExtractLogInfosInterface]=None) -> None:
        self.__path = path
        self.__hash = hash
        self.__extract_log = extract_log
    
    def main(self) -> Dict[str, Union[str, bool]]:
        hash = self.__hash.replace('.mp3', '')
        extract_log = self.__extract_log(
            log_path=join(self.__path, f'{hash}.txt'),
            error_class=ExtractLogInfosError
        )

        try:
            filename = extract_log.get_filename()[8::]
            print(filename)
            estimated_file_size = extract_log.get_estimated_file_size()
            print(estimated_file_size)
            current_file_size = extract_log.get_current_file_size()
            
            if 'completed' in current_file_size:
                json = {
                    'filename': filename,
                    'total': 100,
                    'current': 100,
                    'status': True
                }

            else:
                json = {
                    'filename': filename,
                    'total': estimated_file_size,
                    'current': current_file_size['in conversion'],
                    'status': False
                }

            return json

        except ExtractLogInfosError:
            return {'status': False}

    def set_atributes(self, **kwargs) -> None:
        keys : Tuple[Tuple[str, type]] = (
            ('path', str),
            ('hash', str),
            ('extract_log', ExtractLogInfosInterface),
        )

        for key in keys:
            if key[0] in kwargs:
                AtributeClass.setattr(self, f'__{key[0]}', kwargs[key[0]])