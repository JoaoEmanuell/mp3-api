from typing import Dict, Type
from os.path import basename

from regex import search, compile

from ...interfaces import ExtractLogInfosInterface

class ExtractLogInfos(ExtractLogInfosInterface):
    def __init__(self, log_path: str, error_class: Type[Exception]) -> None:
        self.__log_name = log_path
        self.__error_class = error_class
        self.__seconds = self.get_seconds()
        self.__bitrate = self.get_bitrate()
    
    def get_seconds(self) -> int:
        with open(self.__log_name, 'r') as f:
            file = f.readlines()
            for line in file:
                if 'Duration' in line:
                    # Duration == Duration: 00:23:40.09...
                    duration = line.strip().split(' ')[1][:-1:] # Extract the time and remove ','
                    duration = duration.replace('.', ':')
                    duration = duration.split(':')
                    hour = int(duration[0]) * 3600
                    minute = int(duration[1]) * 60
                    second = int(duration[2])
                    seconds = hour + minute + second
                    return seconds
            return 1

    def get_bitrate(self) -> int:
        # ... Audio ... 44100 Hz ... 128 kb/s...
        bitrate_regex = compile(r'([0-9]{3} kb\/s)') # Regex to extract bitrate
        with open(self.__log_name, 'r') as f:
            file = f.readlines()
            for line in file:
                #if search(hertz_regex, line):
                if 'bitrate' in line:
                    bitrate_str_pos = search(bitrate_regex, line)
                    if bitrate_str_pos == None:
                        raise self.__error_class('Log Error!')
                    else:
                        bitrate_str_pos = bitrate_str_pos.span()
                        bitrate_str = \
                            line[bitrate_str_pos[0]:bitrate_str_pos[1]].replace(' kb/s', '')
                    return int(bitrate_str)
        return 128

    def get_current_file_size(self) -> Dict[str, int]:
        total_file_size_regex = compile(r'(?<=(audio:))(.*)(?=(kBs))')
        current_file_size_regex = compile(r'(?<=(size=))(.*)(?=(kB))')
        cases = (
            ('size', 'in conversion', current_file_size_regex),
            ('audio', 'completed', total_file_size_regex)
        ) # ('key', 'message', regex)
        with open(self.__log_name, 'r') as f:
            file = f.readlines()
            file = [line for line in file if line != '\n'] # Ignore empty lines
            last_line = file[-1].replace(' ', '')

            # Verify error

            if 'Exiting' in last_line:
                raise self.__error_class('Conversion Error!')

            for case, message, regex in cases:
                if case in last_line:
                    pos = search(regex, last_line).span()
                    size = int(last_line[pos[0]:pos[1]])
                    return {message: size}
        raise self.__error_class('Log Error!')
        
    def get_estimated_file_size(self) -> int:
        return int((self.__seconds * self.__bitrate) / 8)

    def get_filename(self) -> str:
        filename_regex = compile(r"(?<=to\s\')(.*)(?=\')")
        with open(self.__log_name, 'r') as f:
            file = f.readlines()
            for line in file:
                if 'Output' in line:
                    pos = search(filename_regex, line).span()
                    if pos == None:
                        raise self.__error_class('Log Error!')
                    filename = line[pos[0] : pos[1]]
                    return basename(filename) # Remove path and return filename
        raise self.__error_class('Log Error!')