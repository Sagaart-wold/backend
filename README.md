# API Șagaart
## Описание:

[Схема базы данных](https://dbdiagram.io/d/Sagaart-667036d9a179551be610c2af)   

### Модель данных:

![Модель данных](doc/model-diagram.svg)

### Схема БД:

![db_scheme](doc/db-Sagaart.png)


**IP тестового сервера**: 158.160.171.226

**Redoc**: http://158.160.171.226/api/v1/redoc/

## Технологии:

[![My Skills](https://skillicons.dev/icons?i=py,docker,postgres,django,nginx,github,postman)](https://skillicons.dev)

## Пользователи

### 1. Суперпользоаватель (вход в админку):

        email: aaa@host2011.com,
        password: alskdjfhg

## Возможности проета:

...

## Что сделано:

Версионирование API

Тестовая БД с данными

1. **Артобъект**

* `api/v1/artobjects/` (**GET**): получить список всех артобъектов
* Фильтр по полям 'category', 'genre', 'style', 'orientation','tag_size', 'colors', 'artist' (id поля):
* Например `api/v1/artobjects/{id}/?category=1` (одно условие)
* Например `api/v1/artobjects/{id}/?genre=1&orientation=1` (выполняются оба условия)

**Пример запроса**

```
GET api/v1/artobjects/
Права доступа: Доступно без токена
Response:

[
    {
        "id": 1,
        "artist": {
            "id": 1,
            "first_name": "Вася",
            "last_name": "Васечкин"
        },
        "vendor": 123,
        "name": "Портрет",
        "status": "В продаже",
        "category": {
            "id": 1,
            "name": "живопись"
        },
        "colors": [
            {
                "id": 1,
                "name": "светлые оттенки"
            },
            {
                "id": 2,
                "name": "темные оттенки"
            }
        ],
        "genre": {
            "id": 1,
            "name": "портрет"
        },
        "width": 100,
        "height": 80,
        "material_art_object": {
            "id": 1,
            "name": "масло"
        },
        "base_art_object": {
            "id": 1,
            "name": "холст"
        },
        "style": {
            "id": 1,
            "name": "готика"
        },
        "main_image": null,
        "is_favourite": false,
        "orientation": "Горизонтальная",
        "tag_size": "до 100 см",
        "actual_price": 33333333
    }
]

``` 

* `api/v1/artobjects/{id}/` (**GET**): получить артобъект по id.

**Пример запроса**
``` 
GET api/v1/artobjects/{id}/
Права доступа: Доступно без токена.
Response:
{
    "id": 1,
    "owner": {
        "id": 1,
        "email": "aaa@host2011.com",
        "first_name": "",
        "last_name": "",
        "phone": null,
        "address": null
    },
    "artist": {
        "id": 1,
        "first_name": "Вася",
        "last_name": "Васечкин",
        "description": "что-то",
        "sex": "М",
        "date_of_birth": "2024-07-01",
        "date_of_death": "2024-07-01",
        "personal_style": false,
        "city_of_birth": {
            "id": 1,
            "name": "Москва",
            "country": {
                "id": 1,
                "name": "Россия"
            }
        },
        "city_of_living": {
            "id": 1,
            "name": "Москва",
            "country": {
                "id": 1,
                "name": "Россия"
            }
        },
        "photo": null,
        "is_favorite": false
    },
    "vendor": 123,
    "name": "Портрет",
    "date_of_creation": "2024-07-01",
    "status": "В продаже",
    "city_sold": {
        "id": 1,
        "name": "Москва",
        "country": {
            "id": 1,
            "name": "Россия"
        }
    },
    "category": {
        "id": 1,
        "name": "живопись"
    },
    "colors": [
        {
            "id": 1,
            "name": "светлые оттенки"
        },
        {
            "id": 2,
            "name": "темные оттенки"
        }
    ],
    "genre": {
        "id": 1,
        "name": "портрет"
    },
    "width": 100,
    "height": 80,
    "material_art_object": {
        "id": 1,
        "name": "масло"
    },
    "base_art_object": {
        "id": 1,
        "name": "холст"
    },
    "style": {
        "id": 1,
        "name": "готика"
    },
    "collection": null,
    "unique": true,
    "art_investment": true,
    "images": [],
    "main_image": null,
    "max_amount": 1,
    "is_favourite": false,
    "orientation": "Горизонтальная",
    "tag_size": "до 40 см",
    "actual_price": 33333333,
    "shows": [
        {
            "name": "Выставка-1",
            "started_at": "2024-07-01",
            "ended_at": "2024-07-02",
            "place": {
                "id": 1,
                "name": "Московская галлерея",
                "city": {
                    "id": 1,
                    "name": "Москва",
                    "country": {
                        "id": 1,
                        "name": "Россия"
                    }
                }
            },
            "personal": false
        },
        {
            "name": "Выставка-2",
            "started_at": "2024-05-01",
            "ended_at": "2024-05-03",
            "place": {
                "id": 1,
                "name": "Московская галлерея",
                "city": {
                    "id": 1,
                    "name": "Москва",
                    "country": {
                        "id": 1,
                        "name": "Россия"
                    }
                }
            },
            "personal": false
        }
    ]
}

``` 


## Работа с Github в команде

Разработка ведется в ветке **develop**


**1. Перейти в ветку develop:**

```
git checkout develop
```

**2. Создать свою ветку для разработки feature и сразу в нее перейти, название ветки <name>/<name_feature>**

```
git checkout -b <name>/<name_feature> 
```

**3. Когда разработка feature закончена, то перед тем как делать запрос на сливание своей ветки в develop проделать следующее:**

   - проверить в какой ветке находитесь:

```
git branch #  Проверили: "Где я?"
* <name>/<name_feature>  # Звездочка указывает в какой вы ветке
master 
develop
```
 - если не в своей ветке, то перейти в нее:

```
 git checkout <name>/<name_feature> 
```
 - если в своей, то все закомитить;
 - затем актуализировать свою ветку по последним изменениям из develop и решить конфликты, если есть:

```
 git rebase develop
```

 - затем отправить свою ветку в git (push).

**4. Перейти на GitHub и сделать “Pull requests” своей feature в ветку develop**

**5. После этого остальных членов команды назначить Reviewer:**
   - если не согласны, то добавляют комменарии;
   - если согласны, то выставляют статус “Approve”.

**6. Когда получены апрувы от всех членов команды, (!)владелец ветки делает “Merge pull request"**


## Запуск среды разработки

### 1. Клонировать docker_wrapper

```
git clone git@github.com:Sagaart-wold/docker-wrapper.git -b development docker-wrapper 
```
или
```
git clone https://github.com/Sagaart-wold/docker-wrapper.git
```


### 2. В папку 'docker_wrapper' склонировать backend

```
git clone git@github.com:Sagaart-wold/backend.git -b develop backend
```
или
```
git clone https://github.com/Sagaart-wold/backend.git -b develop backend
```

### 3. В папку 'docker_wrapper' склонировать frontend

```
git clone git@github.com:Sagaart-wold/frontend.git -b develop frontend
```
или
```
git clone https://github.com/Sagaart-wold/frontend.git -b develop frontend 
```

### 4.  Скопируйте все из файла .env.example в файл .env и актуализируйте данные по необходимости

### 5. В папке 'docker_wrapper' запустить docker-compose.yml:

```
docker-compose up -d
```

### 6. Остановить:

```
docker-compose down
```

### 7. Пересобрать

```
docker-compose build --no-cache --pull
```


## Авторы:  

[Елена](https://github.com/Edelveisx)  

[Виктор](https://github.com/Badmajor)

[Леонид](https://github.com/iceeleoo)

