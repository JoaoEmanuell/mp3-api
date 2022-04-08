from moviepy.editor import AudioFileClip
from pathlib import Path

from .interfaces import ConversorInterface

class Conversor(ConversorInterface):
    @classmethod
    def convert(cls, audio : str) -> None:
        clip = AudioFileClip(audio)
        filename = audio.split("/")[-1].replace(".mp3", "")
        clip.write_audiofile(f'{Path().absolute()}/converteds/{filename}.mp3')
