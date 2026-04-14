# 🐦 Django Tweet App

A full-stack Django-based web application that allows users to create, edit, delete, and search tweets. This project demonstrates core backend development skills including authentication, CRUD operations, media handling, and search functionality.

---

## 🚀 Features

* 🔐 User Authentication (Login, Logout, Register)
* ✍️ Create, Edit, Delete Tweets
* 🖼️ Image Upload with Tweets
* 🔍 Search Tweets (by text and username)
* 🧑‍💻 User-specific tweet management
* 📱 Responsive UI using Bootstrap
* ⚡ Clean and modular Django structure

---

## 🛠️ Tech Stack

* **Backend:** Django (Python)
* **Frontend:** HTML, Bootstrap
* **Database:** SQLite (default)
* **Authentication:** Django built-in auth system

---

## ⚙️ Installation & Setup

### 1️⃣ Clone the repository

```bash
git https://github.com/maddy-abhishek/python-backend-using-Django.git
```

### 2️⃣ Create virtual environment

```bash
python -m venv venv
venv\Scripts\activate   # Windows
```

### 3️⃣ Install dependencies

```bash
pip install -r requirements.txt
```

### 4️⃣ Apply migrations

```bash
cd pythonbackend
python manage.py makemigrations
python manage.py migrate
```

### 5️⃣ Create superuser

```bash
python manage.py createsuperuser
```

### 6️⃣ Run server

```bash
python manage.py runserver
```
---

## 🔍 Search Functionality

* Users can search tweets using the search bar
* Supports:

  * Tweet text search
  * Username search
* Implemented using Django ORM (`icontains`)

---

## 📸 Media Handling

* Users can upload images with tweets
* Images are stored in the `/media/` directory
* Configured using `MEDIA_URL` and `MEDIA_ROOT`

---

## 🔐 Authentication

* Register new users
* Login & Logout functionality
* Only logged-in users can create/edit/delete tweets

---

## 🧠 Learning Outcomes

This project demonstrates:

* Django project structure
* URL routing and views
* Template rendering
* Form handling
* Database models and ORM
* Authentication system
* File uploads and media handling

---

## 🚀 Future Improvements

* ❤️ Like & Comment system
* 🔔 Notifications
* 🤖 AI-based sentiment analysis on tweets
* ⚡ REST API using Django REST Framework
* 🌐 React frontend integration

---

## 🤝 Contributing

Feel free to fork this repo and submit pull requests!

---

## 📜 License

This project is open-source and available under the MIT License.

---

