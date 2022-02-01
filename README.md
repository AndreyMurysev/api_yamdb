
# Проект API для YaMDb 
[![Python](https://img.shields.io/badge/-Python-464646?style=flat-square&logo=Python)](https://www.python.org/)
[![Django](https://img.shields.io/badge/-Django-464646?style=flat-square&logo=Django)](https://www.djangoproject.com/)
[![Django REST Framework](https://img.shields.io/badge/-Django%20REST%20Framework-464646?style=flat-square&logo=Django%20REST%20Framework)](https://www.django-rest-framework.org/)
[![PostgreSQL](https://img.shields.io/badge/-PostgreSQL-464646?style=flat-square&logo=PostgreSQL)](https://www.postgresql.org/)
[![Nginx](https://img.shields.io/badge/-NGINX-464646?style=flat-square&logo=NGINX)](https://nginx.org/ru/)
[![gunicorn](https://img.shields.io/badge/-gunicorn-464646?style=flat-square&logo=gunicorn)](https://gunicorn.org/)
[![docker](https://img.shields.io/badge/-Docker-464646?style=flat-square&logo=docker)](https://www.docker.com/)
[![GitHub%20Actions](https://img.shields.io/badge/-GitHub%20Actions-464646?style=flat-square&logo=GitHub%20actions)](https://github.com/features/actions)
[![Yandex.Cloud](https://img.shields.io/badge/-Yandex.Cloud-464646?style=flat-square&logo=Yandex.Cloud)](https://cloud.yandex.ru/)
[![Django-app workflow](https://github.com/AndreyMurysev/yamdb_final/actions/workflows/yamdb_workflow.yml/badge.svg)]

собирает отзывы (Review) пользователей на произведения (Titles)
## Описание:

Проект YaMDb собирает отзывы (Review) пользователей на произведения (Titles). Произведения делятся на категории: «Книги», «Фильмы», 
«Музыка». Список категорий (Category) может быть расширен администратором (например, можно добавить категорию «Изобразительное.
искусство» или «Ювелирка»).Сами произведения в YaMDb не хранятся, здесь нельзя посмотреть фильм или послушать музыку.

В каждой категории есть произведения: книги, фильмы или музыка. Например, в категории «Книги» могут быть произведения «Винни-Пух и
все-все-все» и «Марсианские хроники», а в категории «Музыка» — песня «Давеча» группы «Насекомые» и вторая сюита Баха. Произведению
может быть присвоен жанр (Genre) из списка предустановленных (например, «Сказка», «Рок» или «Артхаус»). Новые жанры может создавать
только администратор.

Благодарные или возмущённые пользователи оставляют к произведениям текстовые отзывы (Review) и ставят произведению оценку в диапазоне
от одного до десяти (целое число); из пользовательских оценок формируется усреднённая оценка произведения — рейтинг (целое число). На
одно произведение пользователь может оставить только один отзыв.

## Пользовательские роли

| Функционал | Авторизованные пользователи |  Неавторизованные пользователи | Администратор  | Модератор |
|:----------------|:---------:|:---------:|:---------:|:---------:|
| Просматривать описания произведений | :heavy_check_mark: | :heavy_check_mark: | :heavy_check_mark: | :heavy_check_mark: |
| Читать отзывы | :heavy_check_mark: | :heavy_check_mark: | :heavy_check_mark: | :heavy_check_mark: |
| Читать комментарии | :heavy_check_mark: | :heavy_check_mark: | :heavy_check_mark: | :heavy_check_mark: |
| Публиковать отзывы | :heavy_check_mark: | :x: | :heavy_check_mark: | :heavy_check_mark: |
| Ставить оценки произведениям | :heavy_check_mark: | :x: | :heavy_check_mark: | :heavy_check_mark: |
| Комментировать отзывы | :heavy_check_mark: | :x: | :heavy_check_mark: | :heavy_check_mark: |
| Редактировать и удалять свои отзывы | :heavy_check_mark: | :x: | :heavy_check_mark: | :heavy_check_mark: |
| Создавать и удалять произведения, категории и жанры. | :x: | :x: | :heavy_check_mark: | :x: |
| Назначать роли пользователям | :x: | :x: | :heavy_check_mark: | :x: |
| Удалять и редактировать любые отзывы и комментарии | :x: | :x: | :heavy_check_mark: | :heavy_check_mark: |

_Суперюзер Django должен всегда обладать правами администратора, пользователя с правами admin. Даже если изменить пользовательскую роль суперюзера 
 — это не лишит его прав администратора. Суперюзер — всегда администратор, но администратор — не обязательно суперюзер._
 
## Создание пользователя администратором
Пользователя может создать администратор — через админ-зону сайта или через POST-запрос на специальный эндпоинт api/v1/users/ (описание полей 
запроса для этого случая — в документации). В этот момент письмо с кодом подтверждения пользователю отправлять не нужно.
После этого пользователь должен самостоятельно отправить свой email и username на эндпоинт /api/v1/auth/signup/ , в ответ ему должно прийти 
письмо с кодом подтверждения. Далее пользователь отправляет POST-запрос с параметрами username и confirmation_code на эндпоинт /api/v1/auth/token/, 
в ответе на запрос ему приходит token (JWT-токен), как и при самостоятельной регистрации.

## Запуск проекта

- Клонировать репозиторий GitHub (не забываем создать виртуальное окружение и установить зависимости):
[https://github.com/AndreyMurysev/](https://github.com/AndreyMurysev/)

- Cоздать и активировать виртуальное окружение:
```
python3 -m venv env
```

Установить зависимости из файла requirements.txt:

```
python3 -m pip install --upgrade pip
```

```
pip install -r requirements.txt
```

- Сделать миграции, создать суперпользователя и собрать статику:

```
python3 manage.py makemigration
python3 manage.py migrate
python3 manage.py createsuperuser
python3 manage.py collectstatic --no-input 
```

**Проект будет доступен по адресу:** _http://127.0.0.1/api/v1/_  
**Документация API:** _http://127.0.0.1/redoc/_


## Команда разработчиков:
 - https://github.com/AlexeyRudnev
 - https://github.com/Alexander_Niyazov
 - https://github.com/AndreyMurysev

### Для связи с разработчиками:
**email:** _andreimurysev@yandex.ru_  
**telegram:** _@andrey_murysev_  

Авторское право (c) 2021 AAA

Настоящим разрешение предоставляется бесплатно любому лицу, получившему копию
данного программного обеспечения и связанных с ним файлов документации ("Программное обеспечение"), для решения
в Программном обеспечении без ограничений, включая без ограничений права
для использования, копирования, изменения, объединения, публикации, распространения, сублицензии и/или продажи
копии Программного обеспечения, а также для разрешения лицам, которым предоставляется Программное обеспечение
предоставлено для этого при соблюдении следующих условий:

Вышеуказанное уведомление об авторских правах и это уведомление о разрешении должны быть включены во все
копии или существенные части Программного обеспечения.

ПРОГРАММНОЕ ОБЕСПЕЧЕНИЕ ПРЕДОСТАВЛЯЕТСЯ "КАК ЕСТЬ", БЕЗ КАКИХ-ЛИБО ГАРАНТИЙ, ЯВНЫХ ИЛИ
ПОДРАЗУМЕВАЕТСЯ, ВКЛЮЧАЯ, НО НЕ ОГРАНИЧИВАЯСЬ ГАРАНТИЯМИ ТОВАРНОЙ ПРИГОДНОСТИ,
ПРИГОДНОСТЬ ДЛЯ ОПРЕДЕЛЕННОЙ ЦЕЛИ И НЕНАРУШЕНИЕ. НИ В КОЕМ СЛУЧАЕ
АВТОРЫ ИЛИ ПРАВООБЛАДАТЕЛИ НЕ НЕСУТ ОТВЕТСТВЕННОСТЬ ЗА ЛЮБЫЕ ПРЕТЕНЗИИ, УБЫТКИ ИЛИ ДРУГИЕ
ОТВЕТСТВЕННОСТЬ, БУДЬ ТО В РЕЗУЛЬТАТЕ ДЕЙСТВИЯ ДОГОВОРА, ДЕЛИКТА ИЛИ ИНЫМ ОБРАЗОМ, ВЫТЕКАЮЩАЯ ИЗ,
ВНЕ ИЛИ В СВЯЗИ С ПРОГРАММНЫМ ОБЕСПЕЧЕНИЕМ ИЛИ ИСПОЛЬЗОВАНИЕМ ИЛИ ДРУГИМИ СДЕЛКАМИ В
ПРОГРАММНОЕ ОБЕСПЕЧЕНИЕ.
  
