from abc import ABC, abstractclassmethod


class HashInterface(ABC):
    """

    Hash Interface from generate hash

    Args:
        ABC (_type_): _description_

    Raises:
        NotImplementedError: _description_
    """

    @abstractclassmethod
    def generate_random_hash(cls) -> str:
        """_summary_

        Raises:
            NotImplementedError: Not implemented

        Returns:
            str: hash generated with a datetime * a random number, this hash has 8 characters
        """
        raise NotImplementedError
