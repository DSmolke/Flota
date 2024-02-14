FROM python:3.11

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFERED 1

WORKDIR /webapp

COPY Pipfile Pipfile.lock /webapp/

RUN pip install pipenv && pipenv install --system --deploy --ignore-pipfile

COPY . /webapp/
COPY .env /webapp/