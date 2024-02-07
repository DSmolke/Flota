
<div align="center">
  

![logo](https://github.com/DSmolke/Flota/assets/106284705/4699df6e-0a76-4487-9a65-60bfcf34edf1)


[![Flota - microservices](https://img.shields.io/badge/Flota-microservices-2ea44f)](https://github.com/DSmolke/Flota)

### The Fleet is an application designed for managing corporate fleets. Its purpose is to optimize the processes of repairs, insurance, inspections, and vehicle rentals.


![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54) ![Flask](https://img.shields.io/badge/flask-%23000.svg?style=for-the-badge&logo=flask&logoColor=white) ![React](https://img.shields.io/badge/react-%2320232a.svg?style=for-the-badge&logo=react&logoColor=%2361DAFB) ![Gunicorn](https://img.shields.io/badge/gunicorn-%298729.svg?style=for-the-badge&logo=gunicorn&logoColor=white) ![Nginx](https://img.shields.io/badge/nginx-%23009639.svg?style=for-the-badge&logo=nginx&logoColor=white) ![Docker](https://img.shields.io/badge/docker-%230db7ed.svg?style=for-the-badge&logo=docker&logoColor=white) ![MySQL](https://img.shields.io/badge/mysql-%2300f.svg?style=for-the-badge&logo=mysql&logoColor=white)
<br />
<br />
<br />
#### Navigation:
[DEV Stories](#dev-stories) | [Microservices](#microservices) | [How to use](#how-to-use) | [Features](#features) | [How to install & test](#how-to-install--test)


Read in different languages: ![pl](https://github.com/DSmolke/Flota/assets/106284705/36aee71f-8df5-49f0-ab91-71f29fd341d8)[PL](./README.polish.md) ![gb](https://github.com/DSmolke/Flota/assets/106284705/fab2d773-77a0-40b2-bc84-c5af473f26af)[EN](./README.md)


<br />
<br />

![2024-02-0210-15-08-ezgif com-video-to-gif-converter](https://github.com/DSmolke/Flota/assets/106284705/8c6a3d25-41e6-481b-96a8-20c6646eb74a)




https://github.com/DSmolke/Flota/assets/106284705/4205f5be-4b1b-4c26-8517-232cdef0ac07






<br />
<br />

## DEV Stories
<hr>
</div>

### Migrations
At first, my convention was to use a regular alembic to create a global migration for the entire project. This was a suboptimal solution that didn't naturally separate migrations for each of the microservices. That's why I decided to use flask-migrate in each microservice.

### Tests
I conducted them following the guidelines from the documentation - https://flask.palletsprojects.com/en/3.0.x/testing/. For their execution, I used a separate test database. During their execution, I made an effort to clear table rows before each test iteration.

### Cors
At the beginning of development I decided to store CORS policies for any URL with suffix '/*' in separate package inside of 'configuration.py' module. Although this implementation gives more separation between domains of configuration my call is to store it directly in app context, because it gives more compact code. Also storing policies in .env file looks like a 'overkill' to me.

### Coverage and Sphinx Documentation
Once coverage and sphinx docs are generated, they need to be deployed on separate as GitHub pages, and then removed from main repository to avoid messing up with 'Languages' highlights of repository. Here is example before and after:

![image](https://github.com/DSmolke/Flota/assets/106284705/ba27090d-a671-401e-a48b-3114fdd5ccec)
![image](https://github.com/DSmolke/Flota/assets/106284705/d2216eb2-1373-453c-bad9-c9e4e867758d)

### pipenv vs poetry
At this particular project I decided to use pipenv over poetry as it seems to be more stable and up-to-date tool for virtual environments. 

### Loading env variables redundancy
By reviewing code we can see that when it comes to loading environment variables I use python-dotenv package. Because every env file has '.env' filename, theoretically there is no need for using dotenv as pipenv loads those variables by default whenever their path is parallel with Pipfile. But dotenv will definitely will pay off then different naming conventions will see a daylight. Like 'test.env', 'serviceX.env', so I prefer to use this external package. 



<br />
<br />

## Microservices
<hr>


| microservice | wiki                                                         | coverage |
|--------------|--------------------------------------------------------------|----------|
| api-gateway  |                                                              |          |
| cars         | [link](https://dsmolke.github.io/Flota.cars.wiki.github.io/modules.html) | [link](https://dsmolke.github.io/Flota.cars.coverage.github.io/) |


<br/>
<br/>

## How to use
<hr>

[Deployed app](README.md) 🚀

<br/>
<br/>

## Features
<hr>

| Functionality                | State | Demo     |
|------------------------------|-------|----------|
| CRUD Operations on Car       | ✅     | [video]() |
| Authorization                | ✅     | [video]() |
| Registration                 | ✅     | [video]() |
| Authentication via Email     | 🛠️   | [video]() |
| CRUD Operations on Insurance | 🔜    | [video]() |

✅ done
🛠️ in progress
🔜 planned


<br/>
<br/>

## How to install & test
<hr>

#### What is needed 🤔
✔️ [Docker](https://docs.docker.com/get-docker/)
✔️ [NodeJS](https://nodejs.org/en/download)
✔️ [Python 3.11](https://www.python.org/downloads/release/python-3110/)
✔️ [Current .env files](https://www.python.org/downloads/release/python-3110/) - tutorial

<br>

#### Clone repository and enter it's directory 🧐
```
    git clone https://github.com/DSmolke/Flota.git
    cd Flota
```
<br>

#### Add current .env files into required directories 🧐

```
    ......
```

<br>

#### Run docker-compose to create containers 🧐

```
    docker-compose up -d --build
```


<br>

#### Find cars container id, migrate tables using flask_migrate 🧐

```
    docker ps
    docker exec -it <CONTAINER-ID> bash
    cd app
    pipenv run flask --app "create_app:main" db upgrade head
```

<br>

#### Run tests 🧐

```
    cd ..
    pipenv run pytest
```
