# 📝 Task Manager with Django

A simple web-based task management system built with Django, focused on backend fundamentals and real-world application logic.

---

## 🚀 About the Project

This project was developed as part of my learning journey with Django, aiming to build a fully functional application from scratch while applying concepts commonly used in real-world development.

The application allows users to create, edit, organize, and track tasks using different statuses, simulating a basic productivity workflow.

---

## ⚙️ Features

- ✅ Create tasks
- ✏️ Edit tasks
- 🔄 Change task status
- 🗑️ Delete tasks with confirmation
- 📅 Automatic creation timestamp
- 🔄 Automatic last update timestamp
- 🧩 Dynamic status system (separate model)

---

## 🧠 Concepts Applied

- Django ORM (full CRUD operations)
- ForeignKey relationships
- Forms with ModelForm
- View best practices (PRG pattern)
- Environment variable management with `.env`
- Basic Django project structure

---

## 🛠️ Technologies Used

- Python
- Django
- SQLite (default database)
- HTML (Django templates)

---

## 📦 How to Run the Project Locally

### 1. Clone the repository

```bash
git clone https://github.com/milamazim/django-task-manager
cd django-task-manager
```

---

### 2. Create a virtual environment

```bash
python -m venv venv
```

Activate it:

**Linux/Mac**

```bash
source venv/bin/activate
```

**Windows**

```bash
venv\Scripts\activate
```

---

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

---

### 4. Configure environment variables

Create a `.env` file based on `.env.example`:

```env
SECRET_KEY=your_secret_key
DEBUG=True
ALLOWED_HOSTS=127.0.0.1,localhost
```

---

### 5. Apply migrations

```bash
python manage.py makemigrations
python manage.py migrate
```

---

### 6. Create a superuser (optional)

```bash
python manage.py createsuperuser
```

---

### 7. Run the server

```bash
python manage.py runserver
```

Access in your browser:

```
http://127.0.0.1:8000/
```

---

## 📌 Notes

- This project is a work in progress and new features may be added over time.
- This is an initial version (MVP), focused on backend logic and functionality.

---

## 🚀 Future Improvements

- Filter tasks by status
- Group tasks (kanban-style)
- UI/UX improvements
- User authentication

---

## 👩‍💻 About Me

This project is part of my journey learning backend development with Python and Django, with a focus on continuous improvement and building real-world projects.

---
