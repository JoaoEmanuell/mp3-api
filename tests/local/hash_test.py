from sys import path
path.append('../../')

from routes.api.source import Factory
from routes.api.source.interfaces import HashInterface

def test_answer() :
    fac = Factory()

    hash = fac.get_representative(HashInterface)()

    assert isinstance(hash, HashInterface)

    assert len(hash.generate_random_hash()) == 8
