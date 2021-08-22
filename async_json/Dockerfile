FROM python:3
ENV PYTHONUNBUFFERED 1


COPY . /async_json
WORKDIR /async_json

RUN pip3 install -r requirements.txt

ENV FLASK_ENV=development    
ENV FLASK_APP=run.py

EXPOSE 5000