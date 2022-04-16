from time import sleep
from requests import get, post

def upload_audio() -> dict :
    audio = '/home/emanuel/Música/Outros/Rap do The Last of Us 2 - SE EU TE PERDER  Ft Amanda Areia.mp3'
    url = 'http://localhost:5000/api/upload/'
    files = {'file': open(audio, 'rb')}
    r : dict = post(url, files=files).json()
    return r

def get_status(hash : str) -> dict : 
    url = 'http://localhost:5000/api/status/'
    r : dict = get(f'{url}{hash}').json()
    return r

def test_answer() :
    r = upload_audio()

    print(r)
    assert type(r) == dict
    assert r['message'] == 'Audio uploaded successfully'

    sleep(2)
    while True :
        data = get_status(r['hash'])

        try :
            print(f'Data : {data}')
            if data['status'] == True :
                break
        except TypeError as erro:
            print(f"Data Error {erro}\nData : {data}")
            pass
        sleep(3)

test_answer()