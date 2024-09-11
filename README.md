# backend-django-basics
A repo for a basic project using django and getting started on back-end fundamentals.

**Author:** Lucas Zulueta
**Date:** 2024-09-10

---

On this repo I'll be going over the basics of backend.

---

## Index

1. [Section 1: Getting Started](#getting-started)

---

## Section 1: Getting Started

[Back to Index](#index)

### 1. Create the Virtual Environment
First, set up a virtual environment to isolate project dependencies:
```bash
python -m venv env
```
Activate the virtual environment:
```bash
.\env\Scripts\activate
```

### 2. Install Django
Next, install Django to start building your project:
```bash
pip install django
```

### 3. Create a List of Dependencies
To track the dependencies of the project, generate a `requirements.txt` file:
```bash
pip freeze > requirements.txt
```
This will allow for listing and later installation of the required dependencies easily.

### 4. Start the Django Project
Initialize a new Django project named `myproject`:
```bash
django-admin startproject myproject
```

### 5. Create the Skills App
This app will serve as a skills list, which will be used to track the skills you want to learn or use for future projects. Create the app within the project:
```bash
cd .\myproject\
python manage.py startapp skills
```

### 6. Apply Initial Migrations
Finally, set up the initial database by running migrations:
```bash
python manage.py migrate
```

### 7. Run The Project
We can now start the server and check `http://127.0.0.1:8000` to confirm a correct set up.
```bash
python manage.py runserver
```

---
