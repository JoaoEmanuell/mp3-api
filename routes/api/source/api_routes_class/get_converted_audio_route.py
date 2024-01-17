from typing import Dict, Tuple
from urllib.parse import urlparse

from .interfaces import GetConvertedAudioRouteInterface
from ..atributes_manage import AtributeClass


class GetConvertedAudioRoute(GetConvertedAudioRouteInterface):
    def __init__(self, filename: str = None, url_base: str = None):
        self.__filename = filename
        self.__url_base = url_base

    def main(self) -> Dict[str, str]:
        url_base = urlparse(self.__url_base)[0:2]
        url_base = f"{url_base[0]}://{url_base[1]}"

        return {
            "audio": f"{url_base}/static/{self.__filename}",
            "filename": f'{self.__filename.rsplit("/")[-1][8:]}',
        }

    def set_atributes(self, **kwargs):
        keys: Tuple[Tuple[str, type]] = (
            ("filename", str),
            ("url_base", str),
        )

        for key_tuple in keys:
            if key_tuple[0] in kwargs:
                AtributeClass.setattr(self, f"__{key_tuple[0]}", kwargs[key_tuple[0]])
