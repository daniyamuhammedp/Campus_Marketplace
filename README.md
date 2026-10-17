#  Campus Marketplace for Books

A Django and Django REST Framework project where students can list, buy, sell, or exchange textbooks, reference books, and academic notes.

## Features
- Book and Category management
- CRUD operations using Django ORM
- Function-Based Views (FBVs) and Class-Based Views (CBVs)
- Django templates, forms, and admin panel
- Book image uploads and thumbnail generation using Pillow
- Session-based recently viewed books
- REST APIs using serializers, ViewSets, and routers
- User signup and login *(in progress)*

## Tech Stack
- Python
- Django
- Django REST Framework
- SQLite / configured database
- HTML, CSS
- Pillow

## Setup

```bash
git clone <your-repository-url>
cd campus-marketplace
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
```

Open `http://127.0.0.1:8000/` to access the application.

## Objective

A hands-on project to practice Django fundamentals and REST API development by building a campus-focused academic book marketplace.
