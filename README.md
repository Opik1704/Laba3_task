# Лабораторная работа №2

## Очередь задач, поддерживающая итерацию, фильтрацию и потоковую обработку задач.

## Структура проекта
Laba2_task
 <pre>
 ├── src/ # 
 │ ├── init.py # Инициализация 
 │ ├── Task.py # Модель задачи в виде dataclass
 │ ├── TaskQueue.py # Очередь
 │ ├── TaskSource.py # Протокол источника задач
 │ ├── FileTaskSource.py # Источник задач из файла
 │ ├── GeneratorTaskSource.py # Генератор задач
 │ ├── APITaskSource.py # API-заглушка
 │ ├── descriptors.py #Дескрипторы
 │ ├── exceptions.py # Исключения
 │ └── main.py # точка входа в программу
 │
 ├── tests/ # Тесты
 │ ├── init.py # Инициализация тестов
 │ ├── test.py # Тесты 
 ├── .gitignore 
 ├── .pre-commit-config.yaml
 ├── pyproject.toml
 ├── README.md
 ├── requirements.txt
 ├── tasks.json 
 └── uv.lock
  </pre>
## Все сделано реализация протокола итерации, поддержка повторного обхода очереди,реализация ленивых фильтров  по статусу и приоритету,работа с большими объёмами задач.
## Тесты 89%
<img width="641" height="219" alt="image" src="https://github.com/user-attachments/assets/1135de17-224b-4d84-8adf-5b5fb19134d6" />

## Установка 
 ```bash
 $ python -m venv venv
 $ source venv/bin/activate
 
 $ pip install requirements.txt
 $ python -m src.main
```
