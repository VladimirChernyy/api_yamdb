# YaMDb
## Описание
Проект YaMDb собирает отзывы пользователей на различные произведения.
### Технологии
- Python 3.10
- Django 4.2
### Запуск проекта
Скопируйте репазиторий

```$ git clone git@github.com:VladimirChernyy/api_yamdb.git```

Перейдите в директорию проекта

```$ cd api_yamdb```

Установите и активируйте виртуальное окружение

Linux/MacOS

```$ python3 -m venv venv```

```$ source venv/bin/activate```

Windows

```$ python -m venv env```

```$ venv\Scripts\activate.bat```

Установите библиотеки

```$ pip install -r requirements.txt```

Перейдите в приложение проекта

```$ cd tileshop```

Выполните миграции и загрузите базу данных

Linux/MacOS

```$ python3 manage.py makemigrations```

```$ python3 manage.py migrate```

```$ python3 manage.py load_data```

Windows

```$ python manage.py makemigrations```

```$ python manage.py migrate```

```$ python manage.py load_data```

Запустите приложение

```$ python3 manage.py runserver``` для Linux/MacOS

```$ python manage.py runserver``` для Windows

Перейдите по ссылке <a href="http://localhost:8010/docs" target="_blank"> http://localhost:8000/ </a>

### Авторы
- Черный Владимир
- Дмитрий Ермолаев
- Лев Червяков