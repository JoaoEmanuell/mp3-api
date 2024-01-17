from hashlib import sha224
from datetime import datetime
from random import randint

from ..interfaces import HashInterface


class Hash(HashInterface):
    @classmethod
    def generate_random_hash(cls) -> str:
        encoder = "utf-8"
        time = str(datetime.now()).encode(encoder)
        random = str(randint(0, 100000)).encode(encoder)
        return sha224(f"{time}{random}".encode(encoder)).hexdigest()[:8]
