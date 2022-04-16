from requests import post

def upload_audio() -> dict:
    audio = '/home/emanuel/Música/Outros/Rap do The Last of Us 2 - SE EU TE PERDER  Ft Amanda Areia.mp3'
    url = 'http://localhost:5000/api/upload/'
    files = {'file': open(audio, 'rb')}
    r : dict = post(url, files=files).json()
    return r

def test_answer():
    r = upload_audio()
    print(r)
    assert type(r) == dict
    assert r['message'] == 'Audio uploaded successfully'

test_answer()