FROM python:3.8.3-alpine

RUN apk update \
    && apk update && apk add postgresql-dev gcc python3-dev musl-dev \
    && apk add --virtual build-deps \
    && apk add jpeg-dev zlib-dev libjpeg \
    && pip install Pillow \
    && apk del build-deps
