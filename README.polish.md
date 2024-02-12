
<div align="center">
  

![logo](https://github.com/DSmolke/Flota/assets/106284705/4699df6e-0a76-4487-9a65-60bfcf34edf1)


[![Flota - microservices](https://img.shields.io/badge/Flota-microservices-2ea44f)](https://github.com/DSmolke/Flota)

### Flota to aplikacja do obsługi floty firmowej. Ma za zadanie optymalizować procesy napraw, ubezpieczeń, przeglądów oraz wypożyczeń pojazdów


![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54) ![Flask](https://img.shields.io/badge/flask-%23000.svg?style=for-the-badge&logo=flask&logoColor=white) ![React](https://img.shields.io/badge/react-%2320232a.svg?style=for-the-badge&logo=react&logoColor=%2361DAFB) ![Gunicorn](https://img.shields.io/badge/gunicorn-%298729.svg?style=for-the-badge&logo=gunicorn&logoColor=white) ![Nginx](https://img.shields.io/badge/nginx-%23009639.svg?style=for-the-badge&logo=nginx&logoColor=white) ![Docker](https://img.shields.io/badge/docker-%230db7ed.svg?style=for-the-badge&logo=docker&logoColor=white) ![MySQL](https://img.shields.io/badge/mysql-%2300f.svg?style=for-the-badge&logo=mysql&logoColor=white)
<br />
<br />
<br />
#### Nawigacja:
[DEV Stories](#dev-stories) | [Mikroserwisy](#mikorserwisy) | [Jak używać](#jak-używać) | [Funkcjonalności](#funkcjonalności) | [Jak zainstalować i testować](#how-to-install--test)


Czytaj w innych językach: ![gb](https://github.com/DSmolke/Flota/assets/106284705/fab2d773-77a0-40b2-bc84-c5af473f26af)[EN](./README.md) ![pl](https://github.com/DSmolke/Flota/assets/106284705/36aee71f-8df5-49f0-ab91-71f29fd341d8)[PL](./README.polish.md)


<br />
<br />

![2024-02-0210-15-08-ezgif com-video-to-gif-converter](https://github.com/DSmolke/Flota/assets/106284705/8c6a3d25-41e6-481b-96a8-20c6646eb74a)




https://github.com/DSmolke/Flota/assets/106284705/4205f5be-4b1b-4c26-8517-232cdef0ac07






<br />
<br />

## DEV Stories
<hr>
</div>

### Migracje
Na początku moją konwencją było użycie zwykłego alembica do stworzenia globalnej migracji dla całego projektu. Było to nieoptymalne rozwiązanie, które nie rozdzielało w sposób naturalny migracji do każdego z mikroserwisów......

### Testy
Przeprowadziłem je z wytycznych dokumentacji - https://flask.palletsprojects.com/en/3.0.x/testing/ Do ich przeprowadzania użyłem osobnej bazy testowej. W ich egzekucji starałem się czyścić wiersze tabel przed każdą iteracją testu.

### Cors

Na początku procesu rozwoju mikro serwisów postanowiłem przechowywać zasady CORS dla dowolnego adresu URL z sufiksem '/*' w osobnym pakiecie wewnątrz modułu 'configuration.py'. Chociaż ta implementacja zapewnia większe rozdzielenie między domenami konfiguracji, moim zdaniem lepiej je przechowywać bezpośrednio w kontekście aplikacji, ponieważ prowadzi to do bardziej zwartego kodu. Ponadto przechowywanie zasad w pliku .env wydaje mi się nadmiarowe.

### Coverage i Dokumentacja Sphinx
Po wygenerowaniu raportu pokrycia kodu (coverage) oraz dokumentacji Sphinx, należy je umieścić na osobnych stronach GitHub Pages, a następnie usunąć je z głównego repozytorium, aby uniknąć zakłóceń w wyświetlaniu sekcji użytych języków w repozytorium.

![image](https://github.com/DSmolke/Flota/assets/106284705/ba27090d-a671-401e-a48b-3114fdd5ccec)
![image](https://github.com/DSmolke/Flota/assets/106284705/d2216eb2-1373-453c-bad9-c9e4e867758d)

### pipenv vs poetry
W tym konkretnym projekcie postanowiłem użyć pipenv zamiast poetry, ponieważ wydaje się bardziej stabilnym i szybciej aktualizowanym narzędziem do zarządzania środowiskami wirtualnymi.

### Redundancja w ładowaniu zmiennych środowiskowych
Przy przeglądaniu kodu można zauważyć, że do wczytywania zmiennych środowiskowych używam paczki python-dotenv. Ponieważ każdy plik env ma nazwę '.env', teoretycznie nie ma potrzeby korzystania z dotenv, ponieważ pipenv automatycznie wczytuje te zmienne, gdy ich ścieżka jest równoległa z plikiem Pipfile. Jednak dotenv z pewnością się opłaci, gdy zostaną wprowadzone różne konwencje nazewnicze, takie jak 'test.env', 'serviceX.env', dlatego wolę używać tej zewnętrznej paczki.

<br />
<br />

## Mikroserwisy
<hr>


| mikroserwis | wikipedia                                                                | pokrycie testami                                                 |
|-------------|--------------------------------------------------------------------------|------------------------------------------------------------------|
| api-gateway |                                                                          |                                                                  |
| cars        | [link](https://dsmolke.github.io/Flota.cars.wiki.github.io/modules.html) | [link](https://dsmolke.github.io/Flota.cars.coverage.github.io/) |
| mots        | [link]()                                                                 | [link](https://dsmolke.github.io/Flota.mots.coverage.github.io/) |


<br/>
<br/>

## Jak używać
<hr>

[Uruchomiona aplikacja](README.md) 🚀

<br/>
<br/>

## Funkcjonalności
<hr>

| Funkcjonalność                                | Stan | Demonstracja |
|-----------------------------------------------|------|--------------|
| Operacje CRUD na encji Car                    | ✅    | [wideo]()    |
| Autoryzacja                                   | ✅    | [wideo]()    |
| Rejestracja                                   | ✅    | [wideo]()    |
| Autentykacja poprzez email                    | 🛠️  | [wideo]()    |
| Operacje CRUD na encji Mot (Przegląd pojazdu_ | 🔜   | [wideo]()    |

✅ zrobione
🛠️ w trakcie
🔜 zaplanowane


<br/>
<br/>

## Jak zainstalować i testować
<hr>

#### Co jest potrzebne 🤔
✔️ [Docker](https://docs.docker.com/get-docker/)
✔️ [NodeJS](https://nodejs.org/en/download)
✔️ [Python 3.11](https://www.python.org/downloads/release/python-3110/)
✔️ [Aktualne pliki .env](https://www.python.org/downloads/release/python-3110/) - tutorial

<br>

#### Sklonuj repozytorium i wejdź do jego folderu 🧐
```
    git clone https://github.com/DSmolke/Flota.git
    cd Flota
```
<br>

#### Dodaj aktualne pliki .env w odpowiednie miejsca w projekcie 🧐

```
    ......
```

<br>

#### Uruchom docker-compose, aby stworzyć i uruchomić kontenery 🧐

```
    docker-compose up -d --build
```


<br>

#### Znajdź id kontenera cars, zmigruj tabele przy użyciu flask_migrate 🧐

```
    docker ps
    docker exec -it <CONTAINER-ID> bash
    cd app
    pipenv run flask --app "create_app:main" db upgrade head
```

<br>

#### Uruchom testy 🧐

```
    cd ..
    pipenv run pytest
```
