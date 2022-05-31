from sys import path
from typing import Dict
from requests import get
path.append('../../')

from routes.api.source import Factory
from routes.api.source.api_routes_class.interfaces import GetConvertedAudioRouteInterface

def test_answer() :
    fac = Factory()
    assert isinstance(fac, Factory)

    get_converted_audio_route : GetConvertedAudioRouteInterface = fac.get_representative(GetConvertedAudioRouteInterface)()
    get_converted_audio_route.set_atributes(
        filename = '8d40284ftest.mp3', 
        url_base = 'http://localhost:5000'
        )

    response = get_converted_audio_route.main()

    # Is instance 
    assert isinstance(get_converted_audio_route, GetConvertedAudioRouteInterface)

    # Is not instance
    assert not isinstance(get_converted_audio_route, Factory)

    # Type

    assert type(response) == dict

    # Value

    assert response['audio'] == 'http://localhost:5000/static/8d40284ftest.mp3'
    assert response['filename'] == 'test.mp3'

    # App

    response = get('http://localhost:5000/api/converteds/8d40284ftest.mp3')

    json : Dict[str, str] = response.json()

    assert response.status_code == 200

    assert json['audio'] == 'http://localhost:5000/static/8d40284ftest.mp3'
    assert json['filename'] == 'test.mp3'