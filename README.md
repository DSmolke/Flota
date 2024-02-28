
<div align="center">
  

![logo](https://github.com/DSmolke/Flota/assets/106284705/4699df6e-0a76-4487-9a65-60bfcf34edf1)


[![Flota - microservices](https://img.shields.io/badge/Flota-microservices-2ea44f)](https://github.com/DSmolke/Flota)

### The Fleet is an application designed for managing corporate fleets. Its purpose is to optimize the processes of repairs, insurance, inspections, and vehicle rentals.


![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54) ![Flask](https://img.shields.io/badge/flask-%23000.svg?style=for-the-badge&logo=flask&logoColor=white) ![React](https://img.shields.io/badge/react-%2320232a.svg?style=for-the-badge&logo=react&logoColor=%2361DAFB) ![Gunicorn](https://img.shields.io/badge/gunicorn-%298729.svg?style=for-the-badge&logo=gunicorn&logoColor=white) ![Nginx](https://img.shields.io/badge/nginx-%23009639.svg?style=for-the-badge&logo=nginx&logoColor=white) ![Docker](https://img.shields.io/badge/docker-%230db7ed.svg?style=for-the-badge&logo=docker&logoColor=white) ![MySQL](https://img.shields.io/badge/mysql-%2300f.svg?style=for-the-badge&logo=mysql&logoColor=white) ![AWS](https://img.shields.io/badge/AWS-%23FF9900.svg?style=for-the-badge&logo=amazon-aws&logoColor=white)
![Selenium](https://img.shields.io/badge/-selenium-%43B02A?style=for-the-badge&logo=selenium&logoColor=white)
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


### Making API Routes more orthogonal
Creating routes for the "repairs" microservice, I began to wonder if I could introduce an implementation of connecting resources to the API that would be as orthogonal as possible to the application context in which configuration takes place. Orthogonality is the abstraction of a state in which changes in one element of the system do not affect its other elements. The approach I had developed so far was simple. Create a resource, import it into the configuration space, and finally add it to the existing API.

![image](https://github.com/DSmolke/Flota/assets/106284705/9c9f32f3-be72-478a-8bb5-eca8754eb38e)
![image](https://github.com/DSmolke/Flota/assets/106284705/59d5ad04-19cd-42b5-baf7-a123e35e961d)

However, I often had to repeat this procedure for several resources. According to the principle of orthogonality, a change in one module should not necessitate changes outside of it. That's why I created the "RepairEndpointsMapper", where I define the resources I want to attach to the API on the fly.

![image](https://github.com/DSmolke/Flota/assets/106284705/4c8aeb7b-e023-46a2-a139-90867af3e26f)

The API itself is passed when the class is called. This way, the procedure transforms into: Assign the resource along with the path to the mapper, import the mapper, pass the API, and call the "init_endpoints" method. Now, if we want to add a resource, we simply add it to the mapper.

![image](https://github.com/DSmolke/Flota/assets/106284705/8d6e798d-91fd-4f0a-b354-592d1e5cf131)

![image](https://github.com/DSmolke/Flota/assets/106284705/28ba15af-fd06-4558-9072-becd42aae2a6)


### Using `selenium` in a console environment of a Docker container

Automatic settings of a sample `Chrome` web driver in selenium force us to install the Chromium engine in our environment and to use an output device, such as our monitor. However, in order to commercially create automation systems, we need to adapt to working in a Debian environment without extensions emulating a monitor.

Using the example of the `cepik` microservice, which verifies whether our car has valid insurance and inspection, I will demonstrate how I configured selenium objects to work in a Docker container.

#### 1. Installing Google Chrome in a container with Debian
In the `Dockerfile` of our microservice, we invoke commands to install the stable version of Google Chrome.

![image](https://github.com/DSmolke/Flota/assets/106284705/7ead4a30-92a8-4457-81c4-5943a5df6475)

#### 2. Adding arguments to the `selenium.webdriver.chrome.options.Options` object to enable the proper functioning of the Selenium driver
In my code, I created a `ChromeOptionsBuilder`, which provides all the necessary options that we need to add to the object.

![image](https://github.com/DSmolke/Flota/assets/106284705/5c7470fb-17a5-49e0-b6b9-c06091329973)

`--no-sandbox` allows avoiding issues with session creation.

![image](https://github.com/DSmolke/Flota/assets/106284705/56b65f12-b1be-4a23-b5ec-99df50c89f8b)

`--no-screen` disables the need for a screen.

`--disable-dev-shm-usage` changes the cache location from shm to tmp, providing greater flexibility if multiple objects are working on shm.

![image](https://github.com/DSmolke/Flota/assets/106284705/696a7a74-2594-4837-863f-6b1a88cdf87f)

#### The final creation of a driver that works correctly in a Docker container, considering the implementation of the options builder, looks as follows:

![image](https://github.com/DSmolke/Flota/assets/106284705/11af75c7-2735-4f19-a94b-33104b2326d4)


### Where to mock?


When creating unittests, attention should be paid to where to mock functions. For example, if I'm creating a module `a.py` containing the function `get_roberts_name`, mocking should focus on that function.

```python
def get_roberts_name() -> str:
    return 'Robert'
```
Now we create module `b.py`, which will be importing `get_roberts_name`
```python
from a import get_roberts_name

def top_customer() -> str:
    return get_roberts_name()
```

Assuming we want to test `top_customer`, but we don't want to depend on `get_roberts_name`

#### THE CORRECT PLACE OF MOCKING `get_roberts_name` IS `b.py ` AND NOT `a.py`

✅ diff at line 5
```python
import pytest
from b import top_customer

def test_top_customer(mocker) -> None:
    mocker.patch('b.get_roberts_name', side_effect=lambda *args, **kwargs: 'Adam')
    assert top_customer() == 'Adam' # True
```

⛔ diff at line 5
```python
import pytest
from b import top_customer

def test_top_customer(mocker) -> None:
    mocker.patch('a.get_roberts_name', side_effect=lambda *args, **kwargs: 'Adam')
    assert top_customer() == 'Adam' # False
```
<br />
<br />

## Microservices
<hr>


| microservice  | wiki                                                                        | coverage                                                               |
|---------------|-----------------------------------------------------------------------------|------------------------------------------------------------------------|
| api-gateway   |                                                                             |                                                                        |
| cars          | [link](https://dsmolke.github.io/Flota.cars.wiki.github.io/modules.html)    | [link](https://dsmolke.github.io/Flota.cars.coverage.github.io/)       |
| mots          | [link](https://dsmolke.github.io/Flota.mots.wiki.github.io/modules.html)    | [link](https://dsmolke.github.io/Flota.mots.coverage.github.io/)       |
| insurances    | [link](https://dsmolke.github.io/Flota.insurances.wiki.github.io/)          | [link](https://dsmolke.github.io/Flota.insurances.coverage.github.io/) |
| repairs       | [link](https://dsmolke.github.io/Flota.repairs.wiki.github.io/modules.html) | [link](https://dsmolke.github.io/Flota.repairs.coverage.github.io/)    |
| aws-resources |                                                                             |                                                                        |
| cepik         |                                                                             |                                                                        |


<br/>
<br/>

## How to use
<hr>

[Deployed app](README.md) 🚀

<br/>
<br/>

## Features
<hr>

| Functionality                                                  | State | Demo |
|----------------------------------------------------------------|-------|------|
| CRUD Operations on Car                                         | ✅     |      |
| Authorization                                                  | ✅     |      |
| Registration                                                   | ✅     |      |
| Authentication via Email                                       | ✅     |      |
| CRUD Operations on Mot                                         | ✅     |      |
| CRUD Operations on Insurance                                   | ✅     |      |
| Storing static resources in Amazon S3                          | ✅     |      |
| Managing cars repairs                                          | ✅     |      |
| Validating MOT and Insurance using historia.pojazdu.gov        | ✅     |      |
| Generating full car history reports using historia.pojazdu.gov | ✅     |      |
| Loading Cars, Mots, Insurances data from existing sources      | 🔜    |      |

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
