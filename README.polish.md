
<div align="center">
  

![logo](https://github.com/DSmolke/Flota/assets/106284705/4699df6e-0a76-4487-9a65-60bfcf34edf1)


[![Flota - microservices](https://img.shields.io/badge/Flota-microservices-2ea44f)](https://github.com/DSmolke/Flota)

### Flota to aplikacja do obsługi floty firmowej. Ma za zadanie optymalizować procesy napraw, ubezpieczeń, przeglądów oraz wypożyczeń pojazdów


![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54) ![Flask](https://img.shields.io/badge/flask-%23000.svg?style=for-the-badge&logo=flask&logoColor=white) ![React](https://img.shields.io/badge/react-%2320232a.svg?style=for-the-badge&logo=react&logoColor=%2361DAFB) ![Gunicorn](https://img.shields.io/badge/gunicorn-%298729.svg?style=for-the-badge&logo=gunicorn&logoColor=white) ![Nginx](https://img.shields.io/badge/nginx-%23009639.svg?style=for-the-badge&logo=nginx&logoColor=white) ![Docker](https://img.shields.io/badge/docker-%230db7ed.svg?style=for-the-badge&logo=docker&logoColor=white) ![MySQL](https://img.shields.io/badge/mysql-%2300f.svg?style=for-the-badge&logo=mysql&logoColor=white) ![AWS](https://img.shields.io/badge/AWS-%23FF9900.svg?style=for-the-badge&logo=amazon-aws&logoColor=white)
![Selenium](https://img.shields.io/badge/-selenium-%43B02A?style=for-the-badge&logo=selenium&logoColor=white)
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

### Nadanie routom API większej ortogonalności
Tworząc routy dla mikroserwisu „repairs”, zacząłem zastanawiać się, czy jestem w stanie wprowadzić taką implementację podłączania zasobów do API, która będzie jak najbardziej ortogonalna względem kontekstu aplikacji, w którym następuje konfiguracja. Ortogonalność to abstrakcja stanu, w którym zmiany w jednym elemencie systemu nie wpływają na jego inne elementy. Podejście, które dotychczas miałem wypracowane, było proste. Stworzenie zasobu, zaimportowanie go do przestrzeni konfiguracji, a na koniec dodanie go do istniejącego API.

![image](https://github.com/DSmolke/Flota/assets/106284705/8fe74894-25e7-437a-b218-df244871041b)

![image](https://github.com/DSmolke/Flota/assets/106284705/bd00694b-0d9d-4e8d-a3e0-d4eaf1cdf994)



Często jednak musiałem powtarzać tę procedurę dla kilku zasobów. Zgodnie z zasadą ortogonalności, zmiana w jednym module nie powinna wymuszać zmian poza nim. Dlatego stworzyłem „RepairEndpointsMapper”, w którym na bieżąco definiuję zasoby, jakie chcę podpiąć do API. 

![image](https://github.com/DSmolke/Flota/assets/106284705/0548f445-eb90-45b2-a921-d97b391d80e5)


Samo API zostaje przekazane przy wywołaniu klasy. W ten sposób procedura zamienia się w: Przypisz zasób wraz ze ścieżką do mappera, zaimportuj mappera, przekaż API i wywołaj metodę „init_endpoints”. Teraz, jeśli chcemy dodać zasób, po prostu dodajemy go do mappera.

![image](https://github.com/DSmolke/Flota/assets/106284705/f973ad2c-77a3-4e28-8c32-b51147c34934)

![image](https://github.com/DSmolke/Flota/assets/106284705/1924cbef-9b0f-4e4f-9473-6b775f997143)


### Używanie `selenium` w konsolowym środowisku kontenera dockerowego

Automatyczne ustawienia przykładowego web_drivera `Chrome` w selenium wymusza na nas instalowanie silnika chromium w naszym środowisku oraz użycia urządzenia wyjścia, jakim jest nasz monitor. Jednak chcąc komercyjnie tworzyć systemy automatyzacji, musimy dostosować się do pracy w środowisku Debiana bez rozszerzeń emulujących monitor.

Na przykładzie mikroserwisu `cepik`, który weryfikuje czy nasz samochód ma ważne oc i przegląd, pokażę jak skonfigurowałem obiekty `selenium`, do pracy w kontenerze dockerowym.

#### 1. Instalacja google chrome w kontenerze z Debianem

W `Dockerfile` naszego mikroserwisu wywołujemy komendy instalujące stabilną wersję google chrome

![image](https://github.com/DSmolke/Flota/assets/106284705/7ead4a30-92a8-4457-81c4-5943a5df6475)


#### 2. Dodanie do obiektu `selenium.webdriver.chrome.options.Options` argumentów pozwalających na prawidłowe działanie drivera selenium

W swoim kodzie stworzyłem `ChromeOptionsBuilder`, który zapewnia wszystkie potrzebne opcje, które musimy dodać do obiektu

![image](https://github.com/DSmolke/Flota/assets/106284705/5c7470fb-17a5-49e0-b6b9-c06091329973)


`--no-sandbox` pozwala uniknąć problemu z tworzeniem sesji

![image](https://github.com/DSmolke/Flota/assets/106284705/56b65f12-b1be-4a23-b5ec-99df50c89f8b)


`--no-screen` wyłącza potrzebę posiadania ekranu

`--disable-dev-shm-usage` zmienia lokalizację cache z shm na tmp co daje większą elastyczność jeżeli wiele obiektów pracuje na shm

![image](https://github.com/DSmolke/Flota/assets/106284705/696a7a74-2594-4837-863f-6b1a88cdf87f)

#### Finalne stworzenie drivera działającego poprawnie w kontenerze dockerowym, uwzględniając implementację buildera opcji wygląda następująco:

![image](https://github.com/DSmolke/Flota/assets/106284705/11af75c7-2735-4f19-a94b-33104b2326d4)


### Gdzie mockować?

Tworząc unit testy, należy zwracać na miejsce mockowania funkcji. Przykładowo tworzę moduł `a.py`, a w nim funkcję `get_roberts_name`
```python
def get_roberts_name() -> str:
    return 'Robert'
```
Teraz stwórzmy moduł `b.py`, który będzie importował `get_roberts_name`
```python
from a import get_roberts_name

def top_customer() -> str:
    return get_roberts_name()
```
Załóżmy, że chcemy przetestować `top_customer`, ale nie chcemy uzależniać testu od `get_roberts_name`

#### PRAWIDŁOWYM MIEJCEM MOCKOWANIA `get_roberts_name` JEST `b.py ` A NIE `a.py`

✅ różnica w linii 5
```python
import pytest
from b import top_customer

def test_top_customer(mocker) -> None:
    mocker.patch('b.get_roberts_name', side_effect=lambda *args, **kwargs: 'Adam')
    assert top_customer() == 'Adam' # True
```

⛔ różnica w linii 5
```python
import pytest
from b import top_customer

def test_top_customer(mocker) -> None:
    mocker.patch('a.get_roberts_name', side_effect=lambda *args, **kwargs: 'Adam')
    assert top_customer() == 'Adam' # False
```

<br />
<br />

## Mikroserwisy
<hr>


| mikroserwis   | wikipedia                                                                   | pokrycie testami                                                       |
|---------------|-----------------------------------------------------------------------------|------------------------------------------------------------------------|
| api-gateway   |                                                                             |                                                                        |
| cars          | [link](https://dsmolke.github.io/Flota.cars.wiki.github.io/modules.html)    | [link](https://dsmolke.github.io/Flota.cars.coverage.github.io/)       |
| mots          | [link](https://dsmolke.github.io/Flota.mots.wiki.github.io/modules.html)    | [link](https://dsmolke.github.io/Flota.mots.coverage.github.io/)       |
| insurances    | [link](https://dsmolke.github.io/Flota.insurances.wiki.github.io/)          | [link](https://dsmolke.github.io/Flota.insurances.coverage.github.io/) |
| repairs       | [link](https://dsmolke.github.io/Flota.repairs.wiki.github.io/modules.html) | [link](https://dsmolke.github.io/Flota.repairs.coverage.github.io/)    |
| aws-resources |                                                                             |                                                                        |
| cepik         | [link](https://dsmolke.github.io/Flota.cepik.wiki.github.io/modules)        | [link](https://dsmolke.github.io/Flota.cepik.coverage.github.io/)      |


<br/>
<br/>

## Jak używać
<hr>

[Uruchomiona aplikacja](README.md) 🚀

<br/>
<br/>

## Funkcjonalności
<hr>

| Funkcjonalność                                                             | Stan | Demonstracja |
|----------------------------------------------------------------------------|------|--------------|
| Operacje CRUD na encji Car                                                 | ✅    |              |
| Autoryzacja                                                                | ✅    |              |
| Rejestracja                                                                | ✅    |              |
| Autentykacja poprzez email                                                 | ✅    |              |
| Operacje CRUD na encji Mot (Przegląd pojazdu)                              | ✅    |              |
| Operacje CRUD na encji Insurance                                           | ✅    |              |
| Przechowywanie zasobów statycznych w Amazon S3                             | ✅    |              |
| Zarządzenie naprawami samochodów                                           | ✅    |              |
| Walidowanie Przeglądów i OC używając historia.pojazdu.gov                  | ✅    |              |
| Generowanie pełnych raportów histori pojazdu używając historia.pojazdu.gov | ✅    |              |
| Ładowanie Car, Mot, Insurance z istniejących źródeł danych                 | 🔜   |              |
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
