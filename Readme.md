# Запуск проекта


Создаем окружение
```bash
python3 -m venv venv
```

Активируем окружение(Linux/Unix/Mac)
```bash
. venv/bin/activate
```

Ставим зависимости

```bash
pip install -r requirements.txt
```

Применяем миграции
```bash
python manage.py migrate
```

Загружаем товары
```bash
python manage.py loadgoods
```

Копируем статику
```bash
python manage.py collectstatic
```

Запуск dev сервера
```bash
python manage.py runserver
```

