- [Index](#index)
- [Upload](#upload)
- [Status](#status)
- [Convertidos](#convertidos)
- [Delete](#delete)


# Index

Usado para verificar o status da API

**GET**

```
<endpoint>/api/
```

**RETORNO**

```
{
    "message": "Welcome to the API"
}
```

**EXEMPLO**

```
curl -X GET --header "Content-Type: application/json" localhost:80/api/
```

# Upload

Usado para enviar o áudio.

**POST**

```
<endpoint>/api/upload/
```

**RETORNO**

Sucesso:

```
{
    "hash": "<hash gerado pela API>",
    "message": "Audio uploaded successfully"
}
```

Falha:

```
{
    "message": "No file selected"
}
```

**EXEMPLO**

```
curl -X POST --header "Content-Type: multipart/form-data" -F "file=@test.mp3" localhost:80/api/upload/
```

# Status

Usado para verificar o progresso da conversão do áudio

**GET**

```
<endpoint>/api/status/<hash>
```

**RETORNO**

Conversão concluída:

```
{
    "filename": <filename>,
    "total": 100,
    "current": 100,
    "status": True
}
```

Conversão em progresso:

```
{
    "filename": <filename>,
    "total": <estimated file size>,
    "current": <progresso atual da conversão>,
    "status": False
}
```

**Nota:** Para transformar em porcentagem basta usar a fórmula: `(<current> * 100) / <total>`

Erro na extração do progresso:

```
{
    "status": False
}
```

**EXEMPLO**

```
curl -X GET --header "Content-Type: application/json" localhost:80/api/status/<hash>
```

# Convertidos

Usado para coletar o arquivo convertido.

**GET**

```
<endpoint>/api/converteds/<hash>
```

**RETORNO**

```
{
    "audio": "path to audio",
    "filename": "filename"
}
```

**EXEMPLO**

```
curl -X GET --header "Content-Type: application/json" localhost:80/api/converteds/<hash>
```

# Delete

Apaga o arquivo convertido no servidor

**GET**

```
<endpoint>/api/delete/<hash>
```

**RETORNO**

```
{
    "message": "Files deleted successfully"
}
```

**EXEMPLO**

```
curl -X GET --header "Content-Type: application/json" localhost:80/api/delete/<hash>
```
