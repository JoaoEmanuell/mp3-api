from routes.api.source import Factory
from routes.api.source.hash import Hash
from routes.api.source.conversor import Conversor
from routes.api.source.interfaces import FactoryInterface, HashInterface, ConversorInterface

def test_answer() :
    fac = Factory()
    assert isinstance(fac, FactoryInterface)

    # Is instance 

    assert isinstance(fac.get_representative(HashInterface), Hash)
    assert isinstance(fac.get_representative(ConversorInterface), Conversor)

    # Is not instance

    assert not isinstance(fac.get_representative(ConversorInterface), Hash)