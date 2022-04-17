from requests import request
from download import download_file, save_file
from upload import upload_main, get_status
from time import sleep
from requests import get

def main():
    hash : str = upload_main()['hash']

    sleep(2)

    while True :
        data = get_status(hash)

        try :
            print(f'Data : {data}')

            if data['status'] == True :
                break

        except TypeError as erro:
            print(f"Data Error {erro}\nData : {data}")
            pass
        sleep(3)

    print("Downloading...")

    file_url = get(f"http://127.0.0.1:5000/api/converteds/{hash}").json()
    file = download_file(file_url['audio'])
    save_file(file_url['filename'], 'audios' , file)

    print("Downloaded")

main()