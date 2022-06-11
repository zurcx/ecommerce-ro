FROM python:3.8

ENV PYTHONDONTWRITEBUTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /code

RUN python3.8 -m pip install pip
COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . .