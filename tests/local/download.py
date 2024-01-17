from urllib.request import Request, urlopen
from requests import get

def save_file(name : str, dir : str, content : bytes) -> None:
    with open(f'{dir}/{name}', 'wb') as f:
        f.write(content)

def download_file(url : str) -> bytes:
    req = Request(url, headers={'User-Agent': 'Mozilla/5.0'})
    page = urlopen(req).read()
    return page

if __name__ == '__main__' :
    r = get('http://localhost:80/api/converteds/Rap_do_The_Last_of_Us_2_-_SE_EU_TE_PERDER_Ft_Amanda_Areia.mp3').json()
    print(r)
    file = download_file(r['audio'])
    save_file(r['filename'], 'audios' , file)
