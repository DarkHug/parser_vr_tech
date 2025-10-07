# Тестовое задание: Парсер Kaspi магазина

## Описание проекта:

- Скрипт парсит данные с карточки магазина каспи, используя  **Selenium**

### Последовательность в main.py:
1. Извлекается url из `seed.json`
2. Происходит вызов основной функции `parse()`
3. Результат с функции передается в `save_to_db` и `save_to_json`

## Установка и запуск

### !!! Надо указать путь до обычного Chrome и chromedriver в parser.py

### 1. Клонирование репозитория
```
git clone https://github.com/<username>/<repo>.git  
cd app
```

### 2. Установка зависимостей
```pip install -r requirements.txt```

### 3. Настройка окружения
Создайте файл `.env` в папке /app и укажите:  
```
DB_HOST=localhost  
DB_PORT=5432  
DB_NAME=postgres  
DB_USER=postgres  
DB_PASSWORD=postgres

CHROME_PATH=путь_до_вашего_хрома
CHROMEDRIVER_PATH=путь_до_chromedriver
```
### 4. Запуск PostgreSQL через Docker
```docker compose up -d```

### 5. Миграция моделей через Alembic
```alembic revision -m "Initial Migration" --autogenerate```
```alembic upgrade head```

### 6. Запуск проекта
```python main.py```

## Структура проекта
```
parser_vr_tech/  
│  
├── app/  
│   ├── db/  
│   │   ├── __init__.py  
│   │   ├── db_connect.py          # подключение к БД  
│   │  
│   ├── models/  
│   │   ├── __init__.py  
│   │   ├── base.py                 
│   │   ├── product.py            
│   │ 
│   ├── chrome-win64
│   ├── drivers/  
│   │   └── chromedriver.exe  
│   │  
│   ├── export/  
│   │   └── product.json  
│   │   
│   │  
│   ├── migrations/  
│   │   ├── product.json              
│   │   └── env.py  
│   │  
│   ├── parser.py                  # парсер Selenium  
│   ├── saver.py                   # сохранение в БД и JSON  
│   │
│   ├── .env  
│   ├── alembic.ini                    
│   ├── docker-compose.yaml  
│   ├── main.py 
│   ├── parser.py 
│   ├── saver.py 
│   ├── seed.json  
│   ├── requirements.txt  
│   ├── README.md
```
## Модель Product

```
ProductBase
    id 
    name
    category 
    price
    rating 
    reviews
```

## Пример логов
```
{"asctime": "2025-10-07 20:31:41,827", "levelname": "INFO", "name": "sqlalchemy.engine.Engine", "message": "INSERT INTO products (id, name, category, price, rating, reviews) VALUES (%(id)s::UUID, %(name)s, %(category)s, %(price)s, %(rating)s, %(reviews)s)"}
2025-10-07 20:31:41,827 INFO sqlalchemy.engine.Engine [generated in 0.00027s] {'id': UUID('d918110f-6604-4213-91b5-77c9b0c7a853'), 'name': 'Смартфон Samsung Galaxy A16 6 ГБ/128 ГБ серый', 'category': 'Смартфоны', 'price': '96 990 ₸', 'rating': 4.9, 'reviews': 936}```
{"asctime": "2025-10-07 20:31:41,829", "levelname": "INFO", "name": "sqlalchemy.engine.Engine", "message": "COMMIT"}
```

## Дополнение
### Замечения:
- Поздно заметил что можно некоторые объекты вытащить с js части нежели с самого HTML
- Уменьшил бы дублирование WebDriverWait, точнее ловил бы ошибки
- Использовал бы контекстный менеджер в главной функции парсера

Из-за нехватки времени к сожалению:
- Не смог исправить все собственные замечания
- Типизацию с pydantic
- Вынос логов в отдельный json файл

