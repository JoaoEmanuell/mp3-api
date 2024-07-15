- [mp3-api](#mp3-api)
- [Getting Started](#getting-started)
  - [Python](#python)
  - [Docker](#docker)


# mp3-api

A web API made with Flask and FFmpeg used to convert the `mpeg-4 aac` codec to the `mp3` codec.

- [Click here to access the API documentation](./docs/README.md)
- [Click here to access the API documentation (Brazilian Portuguese)](./docs/README-pt-br.md)
- [Click here to access the Docker image](https://hub.docker.com/repository/docker/joaoemanuell/mp3-api/general)

# Getting Started

Clone the repository:

```
git clone https://github.com/JoaoEmanuell/mp3-api.git
```

## Python

**Requirements**

```
python => 3.11
```

Install the dependencies:

```
pip install -r requirements.txt
```

Run the project:

```
flask run --host 0.0.0.0 --port 80
```

## Docker

```
Docker => 24
docker-compose => 1.29
```

Build:

```
docker-compose build
```

Run the container:

```
docker-compose up
```

---