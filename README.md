# Service-home-bookkeeping

[![CI](https://github.com/IlyaVasilevsky47/service_home_bookkeeping/actions/workflows/main.yml/badge.svg?branch=main)](https://github.com/IlyaVasilevsky47/service_home_bookkeeping/actions/workflows/main.yml)

![Screenshot](https://github.com/IlyaVasilevsky47/service_home_bookkeeping/blob/main/readme_img/website.jpg?raw=true)

Service_home_bookkeeping - это удобный сервис для домашней бухгалтерии, который помогает вести личный или семейный бюджет. В недавнем прошлом многие вели бухгалтерию своих домашних финансов в тетрадях или блокнотах, но сегодня большинство людей используют для этого веб-сервисы.

## Возможности:
- Регистрация пользователей - добавление новых пользователей в систему. При регистрации пользователь вводит свой username и пароль;
- Авторизация пользователей - проверка истинности введённых логина и пароля пользователя;
- Список расходов и поступлений - пользователь может сохранить в системе запись о финансовой операции, указав дату, сумму, категорию, план расходов. На странице списка расходов и поступлений отображаются все оставленные пользователем записи, он может их редактировать и удалять;
- Пользователь может просмотреть информацию за другой месяц и года, выбрав другие данные на странице. По выбранному месяцу рассчитывается и выводится общее состояние баланса.

## Запуск проекта:
1. Клонируем проект.
```bash
git clone git@github.com:IlyaVasilevsky47/service_home_bookkeeping.git
```

2. Создаем и активируем виртуальное окружение. 
```bash
python -m venv venv
source venv/scripts/activate
```

3. Обновляем менеджер пакетов pip и устанавливаем зависимости из файла requirements.txt.
```bash
python -m pip install --upgrade pip
pip install -r home_bookkeeping/requirements.txt
```

4. Переходим в папку и создаем базу данных. 
```bash
cd home_bookkeeping
python manage.py migrate 
```

5. Загружаем категории доходов и расходов.
```bash
python manage.py data
```

6. Запускаем проект.
```bash
python manage.py runserver 
```

## Настройка .env:
```conf
DB_ENGINE=django.db.backends.postgresql
DB_NAME=postgres
POSTGRES_USER=postgres
POSTGRES_PASSWORD=postgres
DB_HOST=db
DB_PORT=5432
```

## Запуск через контейнеры:
1. Переходим в папку и запускаем docker-compose.
```bash
cd infra
docker-compose up -d
```
2. Создаем базу данных.
```bash
docker-compose exec web python manage.py migrate
```
3. Загружаем категории доходов и расходов.
```bash
docker-compose exec web python manage.py data
```
4. Собираем всю статику.
```bash
docker-compose exec web python manage.py collectstatic --no-input
```

## Автор:
- Василевский И.А.
- [GitHub](https://github.com/IlyaVasilevsky47)
- [Почта](vasilevskijila047@gmail.com)
- [Вконтакте](https://vk.com/ilya.vasilevskiy47)

## Технический стек
- Python 3.7.9
- Django 2.2.16
- Matplotlib 3.5.3
