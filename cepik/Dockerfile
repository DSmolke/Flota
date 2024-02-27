FROM python:3.11

WORKDIR /webapp

COPY . /webapp
COPY Pipfile Pipfile.lock /webapp/

RUN pip install pipenv && \
    pipenv install --system --deploy --ignore-pipfile

RUN apt-get update && \
    apt-get install -y \
    wget \
    unzip && \
    wget https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb && \
    apt install -y ./google-chrome-stable_current_amd64.deb && \
    rm google-chrome-stable_current_amd64.deb && \
    apt-get clean

