from typing import Tuple, Dict, Union
from json import loads

from .interfaces import GetStatusFileRouteInterface
from ..atributes_manage import AtributeClass

class GetStatusFileRoute(GetStatusFileRouteInterface) :
    def __init__(self, path: str = None, hash: str = None) -> None:
        self.__path = path
        self.__hash = hash
    
    def main(self) -> Dict[str, Union[str, bool]]:
        hash = self.__hash.replace('.mp3', '')

        try : 

            with open(f'{self.__path}{hash}.json', 'r') as f :
                file = f.read()

                if file == '':
                    return {'status' : False}
                else :
                    return dict(loads(file))

        except FileNotFoundError :
            return {'status' : False}

    def set_atributes(self, **kwargs) -> None:
        keys : Tuple[Tuple[str, type]] = (
            ('path', str),
            ('hash', str),
        )

        for key in keys:
            if key[0] in kwargs:
                AtributeClass.setattr(self, f'__{key[0]}', kwargs[key[0]])