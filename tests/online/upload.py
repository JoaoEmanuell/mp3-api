from requests import get, post

def upload_audio() -> dict :
    audio = '/home/emanuel/Música/Outros/Rap do The Last of Us 2 - SE EU TE PERDER  Ft Amanda Areia.mp3'
    url = 'https://joaoemanuellmp3api.fly.dev/api/upload/'
    files = {'file': open(audio, 'rb')}
    r : dict = post(url, files=files).json()
    return r

def get_status(hash : str) -> dict : 
    url = 'https://joaoemanuellmp3api.fly.dev/api/status/'
    r : dict = get(f'{url}{hash}').json()
    return r

def upload_main() -> dict :
    r = upload_audio()

    print(r)
    assert type(r) == dict
    assert r['message'] == 'Audio uploaded successfully'
    return r


if __name__ == '__main__' :
    upload_main()
