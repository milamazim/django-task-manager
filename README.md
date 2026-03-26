# 📝 Django Task Manager

A task management web application built with Django, focused on backend fundamentals, CRUD operations, and production-style deployment.

---

## 🚀 Live Demo

🔗 **App:** [https://django-task-manager-3cth.onrender.com/tasks](https://django-task-manager-3cth.onrender.com/tasks)

🔗 **Admin Panel:** [https://django-task-manager-3cth.onrender.com/admin](https://django-task-manager-3cth.onrender.com/admin)

---

## 📌 Overview

This project was built to practice core backend development concepts using Django in a real application scenario.

The app allows users to create, update, organize, and delete tasks, while also managing task statuses dynamically through a relational data model.

It was also used as a hands-on deployment project, including environment variables, static files configuration, and production setup.

---

## ✨ Features

- ➕ Create tasks
- ✏️ Edit tasks
- 🗑️ Delete tasks with confirmation
- 🔄 Update task status
- ⏱️ Automatic creation timestamp
- 🔁 Automatic last update timestamp
- 🧩 Dynamic status system (separate model)
- 🔐 Django admin panel
- 🌐 Production-ready deployment

---

## 🛠️ Tech Stack

- 🐍 Python
- 🌐 Django
- 🗄️ SQLite
- 🎨 HTML / Django Templates
- 🚀 Gunicorn
- 📦 WhiteNoise
- ☁️ Render

---

## 🧠 Concepts Practiced

- Django ORM
- Full CRUD operations
- ForeignKey relationships
- ModelForm usage
- URL routing and view structure
- Template rendering
- PRG pattern (Post/Redirect/Get)
- Environment variables with `.env`
- Static files in production
- Deployment workflow

---

## 📁 Project Structure

```bash
django-task-manager/
├── app/                # Django project settings
├── tasks/              # Main app
├── build.sh            # Render build script
├── manage.py
├── requirements.txt
└── .env.example
```

---

## 💻 Running Locally

### 1. Clone the repository

```bash
git clone https://github.com/milamazim/django-task-manager.git
cd django-task-manager
```

### 2. Create and activate a virtual environment

#### Linux / macOS

```bash
python -m venv venv
source venv/bin/activate
```

#### Windows

```bash
python -m venv venv
venv\Scripts\activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure environment variables

Create a `.env` file:

```env
SECRET_KEY=your_secret_key
DEBUG=True
ALLOWED_HOSTS=127.0.0.1,localhost
```

### 5. Apply migrations

```bash
python manage.py makemigrations
python manage.py migrate
```

### 6. Create a superuser (optional)

```bash
python manage.py createsuperuser
```

### 7. Run the server

```bash
python manage.py runserver
```

Open:

```bash
http://127.0.0.1:8000/tasks/
```

---

## ☁️ Deployment

This project is deployed on **Render** and includes:

- 📦 Static files handling with WhiteNoise
- ⚙️ Automated build script (`collectstatic` + `migrate`)
- 🔐 Environment variables configuration
- 👤 Automatic admin user creation via env variables

---

## 🔮 Future Improvements

- 🔎 Search tasks
- 🏷️ Filter by status
- 🎨 UI improvements
- 🔗 REST API (Django REST Framework)

---

## 📚 What I Learned

Through this project, I practiced not only Django fundamentals, but also part of the real-world workflow involved in deploying and maintaining a backend application.

That included:

- 🐞 Debugging deployment issues
- ⚙️ Configuring environment variables
- 📦 Handling static files in production
- 🚀 Setting up a production-ready Django project

---

## 👩‍💻 Author

Built by [Camila Marques](https://github.com/milamazim)

Feel free to explore my other projects on GitHub 💙
