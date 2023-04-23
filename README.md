## API для сервиса бронирования переговорок
[![Python](https://img.shields.io/badge/-Python-464646?style=flat&logo=Python&logoColor=ffffff&color=043A6B)](https://www.python.org/)
[![FastAPI](https://img.shields.io/badge/-FastAPI-464646?style=flat&logo=FastAPI&logoColor=ffffff&color=043A6B)](https://fastapi.tiangolo.com/)
[![FastAPI-Users](https://img.shields.io/badge/-FastAPI_Users-464646?style=flat&logo=FastAPI&logoColor=ffffff&color=043A6B)](https://pypi.org/project/fastapi-users/)
[![Pydantic](https://img.shields.io/badge/-Pydantic-464646?style=flat&logo=Pydantic&logoColor=ffffff&color=043A6B)](https://docs.pydantic.dev/)
[![SQLAlchemy](https://img.shields.io/badge/-SQLAlchemy-464646?style=flat&logo=SQLAlchemy%20REST%20Framework&logoColor=ffffff&color=043A6B)](https://www.sqlalchemy.org/)
[![aiosqlite](https://img.shields.io/badge/-aiosqlite-464646?style=flat&logo=aiosqlite&logoColor=ffffff&color=043A6B)](https://pypi.org/project/aiosqlite/)
[![Alembic](https://img.shields.io/badge/-Alembic-464646?style=flat&logo=Alembic&logoColor=ffffff&color=043A6B)](https://alembic.sqlalchemy.org/en/latest/)
[![GoogleAPI](https://img.shields.io/badge/-GoogleAPI-464646?style=flat&logo=GoogleAPI&logoColor=ffffff&color=043A6B)](https://support.google.com/googleapi/?hl=en#topic=7014522)

Приложение предоставляет возможность бронировать помещения на определённый период времени.

### Техническое задание
>Одна большая IT-компания построила крупное офисное здание, и в скором времени в нём будут работать тысячи людей. 
>
>В здании много переговорных комнат, где сотрудники разных отделов время от времени проводят встречи, планёрки, симпозиумы и прочие брейнстормы с вечеринками. 
>Чтобы не было конфликтов и не срывались планы — нужен простой и прозрачный механизм, который позволил бы сотрудникам резервировать переговорки. 
> 
>Ваша задача — написать API для приложения; это приложение предоставит возможность бронировать помещения на определённый период времени. В дальнейшем компания планирует продавать это приложение как часть программного обеспечения для офисных центров, поэтому сделать его нужно асинхронным — чтобы оно работало не просто быстро, а очень быстро!
> 
>Сделать приложение нужно было уже вчера, но чёткого техзадания на проект нет. Тимлид вкратце рассказал, что в приложении должны быть три модели:
> 
> - Модель, описывающая переговорки;
> 
> - Модель, описывающая бронирование (какая переговорка забронирована, кем и на какой период времени);
> 
> - Модель пользователей (с разделением ролей на обычных пользователей и админов системы).
> 
>У пользователя должна быть возможность забронировать свободное помещение на определённый период времени, при этом приложение должно проверять, не забронировал ли уже кто-то это помещение и свободно ли всё время, на которое бронируется эта переговорка. 
>

Клонировать репозиторий и перейти в него в командной строке:

```
git clone https://github.com/MrGorkiy/Room_reservation.git
```

```
cd room_reservation
```

Cоздать и активировать виртуальное окружение:

```
python3 -m venv venv
```

* Если у вас Linux/MacOS

    ```
    source venv/bin/activate
    ```

* Если у вас Windows

    ```
    source venv/scripts/activate
    ```

Установить зависимости из файла requirements.txt:

```
python3 -m pip install --upgrade pip
```

```
pip install -r requirements.txt
```

Создать файл .env:

```
APP_TITLE=Сервис бронирования переговорных комнат
DATABASE_URL=your_database
SECRET=your_secret
FIRST_SUPERUSER_EMAIL=your_email
FIRST_SUPERUSER_PASSWORD=your_password
```

Автогенерация миграций:

```
alembic revision --autogenerate -m "First migration"
```

Применение миграций:

```
alembic upgrade head
```

Запуск проекта:

```
uvicorn app.main:app --reload
```

Документация API:

```
http://127.0.0.1:8000/docs
```

### Технологии:
- Python 3.9
- FastAPI
- SQLAlchemy 1.4
- Git

<!--

```bash
uvicorn app.main:app --reload
```

```bash
alembic revision --autogenerate -m "Add user model"
alembic upgrade head 
```
-->

Автор: ## API для сервиса бронирования переговорок
[![Python](https://img.shields.io/badge/-Python-464646?style=flat&logo=Python&logoColor=ffffff&color=043A6B)](https://www.python.org/)
[![FastAPI](https://img.shields.io/badge/-FastAPI-464646?style=flat&logo=FastAPI&logoColor=ffffff&color=043A6B)](https://fastapi.tiangolo.com/)
[![FastAPI-Users](https://img.shields.io/badge/-FastAPI_Users-464646?style=flat&logo=FastAPI&logoColor=ffffff&color=043A6B)](https://pypi.org/project/fastapi-users/)
[![Pydantic](https://img.shields.io/badge/-Pydantic-464646?style=flat&logo=Pydantic&logoColor=ffffff&color=043A6B)](https://docs.pydantic.dev/)
[![SQLAlchemy](https://img.shields.io/badge/-SQLAlchemy-464646?style=flat&logo=SQLAlchemy%20REST%20Framework&logoColor=ffffff&color=043A6B)](https://www.sqlalchemy.org/)
[![aiosqlite](https://img.shields.io/badge/-aiosqlite-464646?style=flat&logo=aiosqlite&logoColor=ffffff&color=043A6B)](https://pypi.org/project/aiosqlite/)
[![Alembic](https://img.shields.io/badge/-Alembic-464646?style=flat&logo=Alembic&logoColor=ffffff&color=043A6B)](https://alembic.sqlalchemy.org/en/latest/)
[![GoogleAPI](https://img.shields.io/badge/-GoogleAPI-464646?style=flat&logo=GoogleAPI&logoColor=ffffff&color=043A6B)](https://support.google.com/googleapi/?hl=en#topic=7014522)

Приложение предоставляет возможность бронировать помещения на определённый период времени.

### Техническое задание
>Одна большая IT-компания построила крупное офисное здание, и в скором времени в нём будут работать тысячи людей. 
>
>В здании много переговорных комнат, где сотрудники разных отделов время от времени проводят встречи, планёрки, симпозиумы и прочие брейнстормы с вечеринками. 
>Чтобы не было конфликтов и не срывались планы — нужен простой и прозрачный механизм, который позволил бы сотрудникам резервировать переговорки. 
> 
>Ваша задача — написать API для приложения; это приложение предоставит возможность бронировать помещения на определённый период времени. В дальнейшем компания планирует продавать это приложение как часть программного обеспечения для офисных центров, поэтому сделать его нужно асинхронным — чтобы оно работало не просто быстро, а очень быстро!
> 
>Сделать приложение нужно было уже вчера, но чёткого техзадания на проект нет. Тимлид вкратце рассказал, что в приложении должны быть три модели:
> 
> - Модель, описывающая переговорки;
> 
> - Модель, описывающая бронирование (какая переговорка забронирована, кем и на какой период времени);
> 
> - Модель пользователей (с разделением ролей на обычных пользователей и админов системы).
> 
>У пользователя должна быть возможность забронировать свободное помещение на определённый период времени, при этом приложение должно проверять, не забронировал ли уже кто-то это помещение и свободно ли всё время, на которое бронируется эта переговорка. 
>

Клонировать репозиторий и перейти в него в командной строке:

```
git clone https://github.com/MrGorkiy/Room_reservation.git
```

```
cd room_reservation
```

Cоздать и активировать виртуальное окружение:

```
python3 -m venv venv
```

* Если у вас Linux/MacOS

    ```
    source venv/bin/activate
    ```

* Если у вас Windows

    ```
    source venv/scripts/activate
    ```

Установить зависимости из файла requirements.txt:

```
python3 -m pip install --upgrade pip
```

```
pip install -r requirements.txt
```

Создать файл .env:

```
APP_TITLE=Сервис бронирования переговорных комнат
DATABASE_URL=your_database
SECRET=your_secret
FIRST_SUPERUSER_EMAIL=your_email
FIRST_SUPERUSER_PASSWORD=your_password
```

Автогенерация миграций:

```
alembic revision --autogenerate -m "First migration"
```

Применение миграций:

```
alembic upgrade head
```

Запуск проекта:

```
uvicorn app.main:app --reload
```

Документация API:

```
http://127.0.0.1:8000/docs
```

### Технологии:
- Python 3.9
- FastAPI
- SQLAlchemy 1.4
- Git

<!--

```bash
uvicorn app.main:app --reload
```

```bash
alembic revision --autogenerate -m "Add user model"
alembic upgrade head 
```
-->

Автор: ## API для сервиса бронирования переговорок
[![Python](https://img.shields.io/badge/-Python-464646?style=flat&logo=Python&logoColor=ffffff&color=043A6B)](https://www.python.org/)
[![FastAPI](https://img.shields.io/badge/-FastAPI-464646?style=flat&logo=FastAPI&logoColor=ffffff&color=043A6B)](https://fastapi.tiangolo.com/)
[![FastAPI-Users](https://img.shields.io/badge/-FastAPI_Users-464646?style=flat&logo=FastAPI&logoColor=ffffff&color=043A6B)](https://pypi.org/project/fastapi-users/)
[![Pydantic](https://img.shields.io/badge/-Pydantic-464646?style=flat&logo=Pydantic&logoColor=ffffff&color=043A6B)](https://docs.pydantic.dev/)
[![SQLAlchemy](https://img.shields.io/badge/-SQLAlchemy-464646?style=flat&logo=SQLAlchemy%20REST%20Framework&logoColor=ffffff&color=043A6B)](https://www.sqlalchemy.org/)
[![aiosqlite](https://img.shields.io/badge/-aiosqlite-464646?style=flat&logo=aiosqlite&logoColor=ffffff&color=043A6B)](https://pypi.org/project/aiosqlite/)
[![Alembic](https://img.shields.io/badge/-Alembic-464646?style=flat&logo=Alembic&logoColor=ffffff&color=043A6B)](https://alembic.sqlalchemy.org/en/latest/)
[![GoogleAPI](https://img.shields.io/badge/-GoogleAPI-464646?style=flat&logo=GoogleAPI&logoColor=ffffff&color=043A6B)](https://support.google.com/googleapi/?hl=en#topic=7014522)

Приложение предоставляет возможность бронировать помещения на определённый период времени.

### Техническое задание
>Одна большая IT-компания построила крупное офисное здание, и в скором времени в нём будут работать тысячи людей. 
>
>В здании много переговорных комнат, где сотрудники разных отделов время от времени проводят встречи, планёрки, симпозиумы и прочие брейнстормы с вечеринками. 
>Чтобы не было конфликтов и не срывались планы — нужен простой и прозрачный механизм, который позволил бы сотрудникам резервировать переговорки. 
> 
>Ваша задача — написать API для приложения; это приложение предоставит возможность бронировать помещения на определённый период времени. В дальнейшем компания планирует продавать это приложение как часть программного обеспечения для офисных центров, поэтому сделать его нужно асинхронным — чтобы оно работало не просто быстро, а очень быстро!
> 
>Сделать приложение нужно было уже вчера, но чёткого техзадания на проект нет. Тимлид вкратце рассказал, что в приложении должны быть три модели:
> 
> - Модель, описывающая переговорки;
> 
> - Модель, описывающая бронирование (какая переговорка забронирована, кем и на какой период времени);
> 
> - Модель пользователей (с разделением ролей на обычных пользователей и админов системы).
> 
>У пользователя должна быть возможность забронировать свободное помещение на определённый период времени, при этом приложение должно проверять, не забронировал ли уже кто-то это помещение и свободно ли всё время, на которое бронируется эта переговорка. 
>

Клонировать репозиторий и перейти в него в командной строке:

```
git clone https://github.com/MrGorkiy/Room_reservation.git
```

```
cd room_reservation
```

Cоздать и активировать виртуальное окружение:

```
python3 -m venv venv
```

* Если у вас Linux/MacOS

    ```
    source venv/bin/activate
    ```

* Если у вас Windows

    ```
    source venv/scripts/activate
    ```

Установить зависимости из файла requirements.txt:

```
python3 -m pip install --upgrade pip
```

```
pip install -r requirements.txt
```

Создать файл .env:

```
APP_TITLE=Сервис бронирования переговорных комнат
DATABASE_URL=your_database
SECRET=your_secret
FIRST_SUPERUSER_EMAIL=your_email
FIRST_SUPERUSER_PASSWORD=your_password
```

Автогенерация миграций:

```
alembic revision --autogenerate -m "First migration"
```

Применение миграций:

```
alembic upgrade head
```

Запуск проекта:

```
uvicorn app.main:app --reload
```

Документация API:

```
http://127.0.0.1:8000/docs
```

### Технологии:
- Python 3.9
- FastAPI
- SQLAlchemy 1.4
- Git

<!--

```bash
uvicorn app.main:app --reload
```

```bash
alembic revision --autogenerate -m "Add user model"
alembic upgrade head 
```
-->

Автор: [Афанасьев Д.Л.](https://github.com/afanasevdl) - Разработчик 