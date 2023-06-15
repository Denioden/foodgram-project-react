# Foodgram «Продуктовый помощник».

## Установка

Клонировать репозиторий и перейти в него в командной строке:

```
$ git clone https://github.com/Denioden/foodgram-project-react.git
```

Создать и активировать виртуальное окружение:

```
$ python3 -m venv venv
```

* Если у вас Linux/macOS

    ```
    $ source env/bin/activate
    ```

* Если у вас windows

    ```
    $ venv\Scripts\activate.bat
    ```

```
(venv) $ python3 -m pip install --upgrade pip
```

Перейти в директорию log_agregator

```
(venv) $ cd  backend/
```
Установить зависимости из файла requirements.txt:

```
(venv) $ pip install -r requirements.txt
```
Настроить базу данных postgresql. Описано ниже. 

Выполнить миграции:
```
(venv) $ python3 manage.py makemigarations
(venv) $ python3 manage.py migration
```

### Создаём базу данных:

- Вызовите утилиту psql.
```
(venv) $ sudo -u postgres psql
```
- Теперь через psql создайте базу данных, например foodgram
```
postgres=# CREATE DATABASE foodgram;
```
- Создайте пользователя например foodgram_user и придумайте пароль.
```
postgres=#CREATE USER foodgram_user WITH ENCRYPTED PASSWORD 'foodgram_password';
``` 
- Дайте пользователю foodgram_user все права при работе с базой foodgram. 
```
- postgres=#GRANT ALL PRIVILEGES ON DATABASE foodgram TO foodgram_user;
```
- Выйдите из psql.
``` 
postgres=#\q
```
     
Создайте .env файл. Директория_проекта/backend/foodgram/.env
Добавьте в файл настройки подключения к базе данных:

- Укажите, что используете postgresql.
    DB_ENGINE=django.db.backends.postgresql

- Укажите имя созданной базы данных.
    DB_NAME=foodgram

- Укажите имя пользователя.
    POSTGRES_USER=foodgram_user

- Укажите пароль для пользователя.
    POSTGRES_PASSWORD=foodgram_password

- Укажите localhost.
   DB_HOST=127.0.0.1

- Укажите порт, для подключения к базе.
    DB_PORT=5432 


## Запуск проекта локально.

- Проверить что виртуальное окружение активировано.
- Переходим в директорию, где находится файл manage.py
     
- Создаём суперпользователя:
    ```
    (venv) $ python manage.py createsuperuser

    ```
- вводим имя, пароль, повтор пароля:
    ```
    (venv) $ Email addres: ivanov@yandex.ru
    (venv) $ Username: admin
    (venv) $ First name: ivan
    (venv) $ Last name: ivanov
    (venv) $ Password: admin
    (venv) $ Password (again): admin
    ```

- Активируем локальный сервер.
    ```
    python3 manage.py runserver
    ```

- Переходим в директорию frontend/ 
    ```
    cd frontend
    ```

- Запускаем frontend
    ```
    npm install
    npm run build
    npm start
    ```