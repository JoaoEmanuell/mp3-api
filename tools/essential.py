from typing import List
from os import mkdir, remove, listdir
from pathlib import Path
from .interfaces import EssentialInterface

class Essential(EssentialInterface):

    def create_dirs(self, dirs: List[str]):
        for dir in dirs :
            if not Path(dir).exists():
                mkdir(dir)

    def delete_old_files(self, dirs: List[str]):
        for dir in dirs :
            for file in listdir(dir):
                remove(f'{dir}/{file}')

dirs_list = ['audios', 'static', 'status']
essential = Essential()
essential.create_dirs(dirs_list)
essential.delete_old_files(dirs_list)