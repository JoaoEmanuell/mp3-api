from sys import path
from requests import get
from typing import Dict, Union
from pathlib import Path
from time import sleep
path.append('../../')

from routes.api.source import Factory
from routes.api.source.api_routes_class.interfaces import GetStatusFileRouteInterface

def test_answer() :
    fac = Factory()

    # Class Route

    hash = 'd8d2d2b1Rap_do_The_Last_of_Us_2_-_SE_EU_TE_PERDER_Ft_Amanda_Areia.mp3' # Insert hash

    get_status_file_route : GetStatusFileRouteInterface = fac.get_representative(GetStatusFileRouteInterface)()
    get_status_file_route.set_atributes(
        path = f'{Path().absolute()}/status/',
        hash = hash
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

    while True :

        response = get(f'http://localhost:5000/api/status/{hash}')

        json : Dict[str, Union[str, bool]] = response.json()

        assert response.status_code == 200

        if 'filename' in json :

            assert json['filename'] == hash[8::].replace('.mp3', '')

        if json['status'] == True :
            break

        sleep(5)