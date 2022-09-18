- [Api](#api)
  - [Index](#index)
  - [Upload](#upload)
  - [Converteds](#converteds)
  - [Status](#status)
  - [Delete](#delete)

# Api

Api é a rota responsável por gerenciar a api de conversão para mp3, ela é o núcleo do projeto.

Cada rota retorna um json.

## Index

**Métodos:**

GET

**Descrição:**

Rota padrão da api, usada para verificar se ela está funcionando.

**Retorno:**

Json, uma mensagem de boas vindas a api.

    {
        'message': 'Welcome to the API'
    }

## Upload

**Métodos:**

POST

**Descrição:**

Rota responsável pelo recebimento do arquivo de áudio.

Por ser uma rota do tipo **POST**, você deve enviar o arquivo no campo **FILE** do corpo do request.

Exemplo com python:

    from requests import post

    audio = path/to/audio.mp3
    url = 'url/api/upload/'
    files = {
        'file': open(audio, 'rb')
    }
    r = post(url, files=files)

**Retorno:**

Json, contendo o hash do arquivo enviado, esse hash será utilizado para verificar status relacionado ao arquivo e deletar o mesmo do servidor.

Se o arquivo estiver completo:

    {
        'message': 'Audio uploaded successfully',
        'hash': 'hash'
    }

Se o arquivo estiver incompleto:

    {
        'message': 'No file selected'
    }

## Converteds

**Métodos:**

GET

**Descrição:**

Rota responsável por retornar o caminho para o arquivo convertido.

**Parâmetros:**

filename: str # Hash do arquivo, disponibilizado por [upload](#upload)

**Retorno:**

Json, contem o caminho para o áudio e o nome do arquivo.

    {
        'audio': 'url/static/audio.mp3',
        'filename': 'filename'
    }

## Status

**Métodos:**

GET

**Descrição:**

Rota responsável por verificar o status de conversão do arquivo.

**Parâmetros:**

hash: str # Hash do arquivo, disponibilizado por [upload](#upload)

**Retorno:**

Json.

Caso o arquivo tenha sido convertido com sucesso:

    {
        'filename': 'filename',
        'total': 100,
        'current': 100,
        'status': True
    }

Caso o arquivo ainda esteja em conversão:

    {
        'filename': 'filename',
        'total': total,
        'current': current,
        'status': False
    }

Caso tenha ocorrido um error na extração do log:

    {
        'status': False
    }

## Delete

**Métodos:**

GET

**Descrição:**

Rota responsável por deletar o áudio enviado, o áudio convertido e o log do sistema.

**Parâmetros:**

hash: str # Hash do arquivo, disponibilizado por [upload](#upload)

**Retorno:**

Json

    {
        'message': 'Files deleted successfully'
    }