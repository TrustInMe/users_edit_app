FROM python:3
ENV PYTHONUNBUFFERED 1


COPY . /users_edit_app
WORKDIR /users_edit_app

RUN pip3 install -r requirements.txt

ENV FLASK_ENV=development    
ENV FLASK_APP=run.py

EXPOSE 5000