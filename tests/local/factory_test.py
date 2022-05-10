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
    print(fac.get_representative(HashInterface)())
    assert isinstance(fac.get_representative(HashInterface)(), Hash)
    assert isinstance(fac.get_representative(ConversorInterface)(), Conversor)

    # Is not instance

    assert not isinstance(fac.get_representative(ConversorInterface)(), Hash)

    ## Delete Files Route

    assert isinstance(fac.get_representative(DeleteFilesRouteInterface)(), DeleteFilesRoute)

    # Is not instance
    
    assert not isinstance(
        fac.get_representative(DeleteFilesRouteInterface)(), Hash)

    delete_files_route : DeleteFilesRouteInterface = fac.get_representative(
        DeleteFilesRouteInterface)(hash = '123')

    delete_files_route.set_atributes(hash = '123')

if __name__ == '__main__' : 
    test_answer()