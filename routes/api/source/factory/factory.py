# Global imports

from typing import Type, Tuple
from abc import ABC

# Local imports

from ..interfaces import FactoryInterface
from ..hash import Hash
from ..conversor import ConversorFfmpeg
from ..conversor.ffmpeg import ExtractLogInfos
from ..api_routes_class import DeleteFilesRoute, UploadAudioRoute, GetConvertedAudioRoute, GetStatusFileRoute

class Factory(FactoryInterface) :
    def __init__(self) -> None:
        self.__representatives : Tuple[ABC] = (
            Hash,
            ConversorFfmpeg,
            ExtractLogInfos,

            # Routes

            DeleteFilesRoute,
            UploadAudioRoute,
            GetConvertedAudioRoute,
            GetStatusFileRoute,
        )

    def get_representative(self, interface: Type[ABC]) -> ABC:

        for representative in self.__representatives :
            try : 
                if issubclass(representative, interface) :
                    return representative
            except TypeError as error:
                print(error)

        raise ValueError(f'{interface} has no representative')
