FROM python:3.11-alpine3.15

WORKDIR /app
COPY . /app

# Python

RUN pip install --no-cache-dir --upgrade pip setuptools wheel

RUN pip3 --no-cache-dir install -r requirements.txt

# Ffmpeg version 4.4.1

RUN apk add --no-cache ffmpeg

# Bash

RUN apk add --no-cache --upgrade bash

EXPOSE 80

ENTRYPOINT [ "flask" ]

CMD [ "run", "--host", "0.0.0.0", "--port", "80" ]
