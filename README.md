# my_resume

my_resume (моё резюме) - проект, позволяющий легко создать web-страницу 
пользователя. Здесь уже прописан шаблон с разделами: обо мне, образование, 
навыки, опыт, портфолио, а также кнопка "скачать PDF", позволяющая скачать
печатную версию резюме. Просто заполните всю информацию в админ-зоне и
получите готовую сраницу без необходимости делать верстку. Также можно обновлять
и дополнять данные через админку и они будут отображаться на странице.

Версия проекта доступна по адресу [miskhozhev.ru](https://miskhozhev.ru)

## Стек технологий

* [Python 3.9+](https://www.python.org)
* [Django 4.1.10](https://www.djangoproject.com)
* [django-bootstrap5 22.2](https://django-bootstrap5.readthedocs.io)
* [django-compressor==4.4](https://django-compressor.readthedocs.io)
* [HTML, CSS](https://developer.mozilla.org/ru/)
* [python-dotenv==1.0.1](https://pypi.org/project/python-dotenv/)

## Развертывание проекта

Для локального развертывания проекта клонируйте репозиторий:

```console
git clone https://github.com/OlegMiskhozhev/my_resume.git
```

В каталоге проекта создайте и активируйте вирутальное окружение:
```console
python -m venv venv
source venv/bin/activate  #Для Linux и MacOS
source venv/Scripts/activate  #Для Windows
```

Установите зависимости:
```console
python -m pip install --upgrade pip
pip install -r requiremts.txt
```

Создате файл .env для хранения закрытой информации
(ключи, имена пользователей, пароли):
```console
touch .evn
```

Открыте файл .env и укажите в нем следующие данные:
```console
SECRET_KEY=some_key                 #Укажите свой ключ для шифрования в Django
ALLOWED_HOSTS=localhost,127.0.0.1   #Для развертывания на сервере, добавьте ip
                                    #сервера и имя хоста
```

Перейдите в каталог my_resume выполните миграции и создайте суперпользователя:
```console
cd my_resume
python manage.py migrate
python manage.py createsuperuser
```

Перейдите в каталог resume:
```console
cd resume
```

Откройте файл view.py и в сроке ниже измените значение параметра username
на имя пользовтаеля только что созданнаого суперпользователя:
```
        user = get_object_or_404(User, username='your_superuser')
```

Вернитесь в каталог my_resume и запустите локальный сервер:
```console
cd ..
python manage.py runserver
```

Откройте браузер и перейдите по адресу: http://127.0.0.1:8000/admin
Заполните все разделы. После чего готовый результат можно буде увидеть по
адресу http://127.0.0.1:8000/

## Планируемые доработки

Реализация обратной связи, в настоящее время кнопка находится в разделе Опыт
и не активна.
Реализация автоматического заполнения базы данных через JSON файл.

## Авторы
[OlegMiskhozhev](https://github.com/OlegMiskhozhev)