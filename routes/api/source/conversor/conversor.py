from os import system
from os.path import join, basename
from pathlib import Path
from multiprocessing import Process

from .moviepy import AudioFileClip
from ..interfaces import ConversorInterface

class Conversor(ConversorInterface):
    @classmethod
    def convert(cls, audio : str) -> None:
        clip = AudioFileClip(audio)
        filename = audio.split("/")[-1].replace(".mp3", "")
        clip.write_audiofile(f'{Path().absolute()}/static/{filename}.mp3')

class ConversorFfmpeg(ConversorInterface):
    @classmethod
    def convert(cls, audio: str) -> None:
        absolute_path = Path().absolute()
        ffmpeg_sh_path = join(absolute_path, 'ffmpeg', 'ffmpeg.sh')
        filename = basename(audio).replace('.mp3', '')
        converted_audio_path = join(absolute_path, 'static', f'{filename}.mp3')
        log_path = join(absolute_path, 'status', f'{filename}.txt')
        ffmpeg_command = f'{ffmpeg_sh_path} {audio} {converted_audio_path} {log_path}'
        
        process = Process(target=system, args=(ffmpeg_command, ))
        process.start()