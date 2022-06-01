from sys import path
from requests import get
from typing import Dict
from pathlib import Path
path.append('../../')

from routes.api.source import Factory
from routes.api.source.api_routes_class.interfaces import GetStatusFileRouteInterface

def test_answer() :
    fac = Factory()

    # Class Route

    get_status_file_route : GetStatusFileRouteInterface = fac.get_representative(GetStatusFileRouteInterface)()
    get_status_file_route.set_atributes(
        path = f'{Path().absolute()}/status/',
        hash = '8d40284ftest.mp3'
    )

    response = get_status_file_route.main()

    # Is instance 
    assert isinstance(get_status_file_route, GetStatusFileRouteInterface)

    # Is not instance
    assert not isinstance(get_status_file_route, Factory)

    # Type
    assert type(response) == dict

    # Value
    assert response['status'] == False

    # App
    
    '''response = get('http://localhost:5000/api/status/8d40284ftest.mp3')

    json : Dict[str, str] = response.json()

    assert response.status_code == 200

    assert json['status'] == 'converting'
    assert json['filename'] == 'test.mp3'''