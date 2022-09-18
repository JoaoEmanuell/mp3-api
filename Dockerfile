FROM python:3.8.10-alpine

WORKDIR /app
COPY . /app

# Python

RUN pip install --no-cache-dir --upgrade pip setuptools wheel

RUN pip3 --no-cache-dir install -r requirements.txt

# Ffmpeg

RUN apk add --no-cache ffmpeg

# Bash

RUN apk add --no-cache --upgrade bash

ENTRYPOINT [ "flask" ]

CMD [ "run", "--host", "0.0.0.0", "--port", "8080" ]
