FROM python:3.4
ENV PYTHONBUFFERED 1

WORKDIR /opt
COPY requirements.txt ./
RUN pip install -r requirements.txt

ADD pkg /app
WORKDIR /app
