from sys import path
path.append('../../')

from routes.api.source import Factory
from routes.api.source.api_routes_class.interfaces import GetConvertedAudioRouteInterface
from routes.api.source.api_routes_class import GetConvertedAudioRoute

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
    assert response['audio'] == 'http://localhost:5000/static/8d40284ftest.mp3'
    assert response['filename'] == 'test.mp3'