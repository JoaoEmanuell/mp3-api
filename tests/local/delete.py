from requests import get
from sys import argv

def test_answer() :

    url = 'http://localhost:80/api/delete/'

    hash = argv[1]

    r = get(f'{url}{hash}').json()
    
    print(r)

if __name__ == '__main__' :
    test_answer()
