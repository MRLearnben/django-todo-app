# Django ToDo App

## Description
A simple ToDo list web app built with Django.

## Features
- List, add, update, delete todos
- Toggle completed status
- Success messages

## Screenshots
![List View](screenshot1.png)  # Upload images to repo
![Add Todo](screenshot2.png)

## How to Run Locally (Without Docker)
1. Clone repo: `git clone https://github.com/yourusername/django-todo-app.git`
2. `cd django-todo-app`
3. `python -m venv venv`
4. Activate venv
5. `pip install -r requirements.txt`
6. `python manage.py migrate`
7. `python manage.py runserver`

## How to Run with Docker
1. Clone repo
2. `docker build -t todo-app .`
3. `docker run -p 8000:8000 todo-app`
Or `docker-compose up`

## Tech Stack
- Django (Python framework)
- SQLite (database)
- Bootstrap (styling)
- Docker (containerization)
