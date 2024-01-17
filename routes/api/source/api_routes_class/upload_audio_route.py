from werkzeug.utils import secure_filename
from werkzeug.datastructures import FileStorage
from threading import Thread
from typing import Tuple, Dict

from ..atributes_manage import AtributeClass
from .interfaces import UploadAudioRouteInterface
from ..interfaces import ConversorInterface, HashInterface


class UploadAudioRoute(UploadAudioRouteInterface):
    def __init__(
        self,
        path: str = None,
        file: FileStorage = None,
        conversor: ConversorInterface = None,
        hash: HashInterface = None,
    ) -> None:
        self.__path = path
        self.__file = file
        self.__conversor = conversor
        self.__hash = hash

    def set_atributes(self, **kwargs) -> None:
        keys: Tuple[Tuple[str, type]] = (
            ("path", str),
            ("file", FileStorage),
            ("conversor", ConversorInterface),
            ("hash", HashInterface),
        )

        for key_tuple in keys:
            if key_tuple[0] in kwargs:
                AtributeClass.setattr(self, f"__{key_tuple[0]}", kwargs[key_tuple[0]])

    def main(self) -> Dict[str, str]:
        hash = self.__hash.generate_random_hash()
        self.__filename = f"{hash}{secure_filename(self.__file.filename)}"

        if self.__filename == "":
            return {"message": "No file selected"}

        self.__file.save(f"{self.__path}{self.__filename}")

        self.private__start_conversion()

        return {"message": "Audio uploaded successfully", "hash": self.__filename}

    def private__start_conversion(self) -> None:
        Thread(
            target=self.__conversor.convert, args=(f"{self.__path}{self.__filename}",)
        ).start()
