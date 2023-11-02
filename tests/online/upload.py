from requests import get, post

def upload_audio() -> dict :
    audio = './audios/Rap_do_The_Last_of_Us_2_-_SE_EU_TE_PERDER_Ft_Amanda_Areia.mp3'
    url = 'https://mp3-api.onrender.com/api/upload/'
    files = {'file': open(audio, 'rb')}
    r : dict = post(url, files=files).json()
    return r

def get_status(hash : str) -> dict : 
    url = 'https://mp3-api.onrender.com/api/status/'
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
