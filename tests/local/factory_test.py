from sys import path
path.append('../../')
from routes.api.source import Factory
from routes.api.source.hash import Hash
from routes.api.source.conversor import Conversor
from routes.api.source.interfaces import FactoryInterface, HashInterface, ConversorInterface
from routes.api.source.api_routes_class.interfaces import DeleteFilesRouteInterface
from routes.api.source.api_routes_class import DeleteFilesRoute

def test_answer() :
    fac = Factory()
    assert isinstance(fac, FactoryInterface)

    # Is instance 

    # assert isinstance(fac.get_representative(HashInterface), Hash)
    # assert isinstance(fac.get_representative(ConversorInterface), Conversor)

    # Is not instance

    # assert not isinstance(fac.get_representative(ConversorInterface), Hash)

    ## Delete Files Route

    assert isinstance(fac.get_representative(DeleteFilesRouteInterface, '123'), DeleteFilesRoute)

    # Is not instance
    
    assert not isinstance(fac.get_representative(DeleteFilesRouteInterface), Hash)

if __name__ == '__main__' : 
    test_answer()