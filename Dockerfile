FROM python:3.8.10-alpine

WORKDIR /app
COPY . /app

# Python
# Numpy installation

RUN pip install --no-cache-dir --upgrade pip setuptools wheel
# RUN apk --no-cache add musl-dev linux-headers g++
# RUN pip3 install numpy==1.22.3 # This process is slower

RUN pip3 --no-cache-dir install -r requirements.txt

# Ffmpeg

RUN apk add --no-cache ffmpeg

# Bash


RUN apk add --no-cache --upgrade bash

ENTRYPOINT [ "python3" , "-m" ]
CMD [ "flask", "run", "--host=0.0.0.0" ]