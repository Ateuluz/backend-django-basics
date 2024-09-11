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

1. The first thing to do is to create the environment in which the work will be done by using ```python -m venv env``` command on the terminal.
``` bash
.\env\Scripts\activate
```

2. Now, installing `django` will be the next step.
``` bash
pip install django
```

3. Create list of dependencies of the project.
``` bash
pip freeze > requirements.txt` will allow for listing dependencies of the project.
```

4. Now we start the project.
``` bash
django-admin startproject myproject
```

5. The app will be oriented towards serving as a skill list I will later use to decide what skills to learn/use for future projects.
``` bash
cd .\myproject\
python manage.py startapp skills
```

6. At last, initial migrations will be made to setup the database.
``` bash
python manage.py migrate
```

---
