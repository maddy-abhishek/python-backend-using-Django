# 🐦 Django Tweet App

A full-stack Django-based web application that allows users to create, edit, delete, and search tweets. This project demonstrates core backend development skills including authentication (OAuth2, JWT, Email Verification), CRUD operations, and advanced API security.

---

## 🚀 Features

* 🔐 **Advanced Authentication**
  * OAuth2 Social Login (Google)
  * JWT Token-based Authentication
  * Email Verification with Celery
  * User Registration & Login
* ✍️ Create, Edit, Delete Tweets
* 🖼️ Image Upload with Tweets
* 🔍 Search Tweets (by text and username)
* 🧑‍💻 User-specific tweet management
* 📱 Responsive UI using Bootstrap
* ⚡ Clean and modular Django structure
* 🔄 REST API with Django REST Framework

---

## 🛠️ Tech Stack

* **Backend:** Django (Python)
* **Frontend:** HTML, Bootstrap
* **Database:** SQLite (default)
* **Authentication:** 
  * Django built-in auth system
  * OAuth2 (Google Login)
  * JWT (JSON Web Tokens)
* **Email:** Celery + Redis for async email verification
* **API:** Django REST Framework

---

## ⚙️ Installation & Setup

### 1️⃣ Clone the repository

```bash
git clone https://github.com/maddy-abhishek/python-backend-using-Django.git
```

### 2️⃣ Create virtual environment

```bash
python -m venv venv
venv\Scripts\activate   # Windows
# or
source venv/bin/activate  # macOS/Linux
```

### 3️⃣ Install dependencies

```bash
pip install -r requirements.txt
pip install -r requirements_auth.txt
```

### 4️⃣ Set up environment variables

Create a `.env` file in the project root:

```env
# OAuth2 Google Credentials
GOOGLE_OAUTH_KEY=your_google_oauth_key
GOOGLE_OAUTH_SECRET=your_google_oauth_secret

# JWT Configuration
JWT_SECRET_KEY=your_secret_key_here

# Email Configuration
EMAIL_HOST=smtp.gmail.com
EMAIL_PORT=587
EMAIL_USE_TLS=True
EMAIL_HOST_USER=your-email@gmail.com
EMAIL_HOST_PASSWORD=your-app-password

# Celery & Redis
CELERY_BROKER_URL=redis://localhost:6379/0
CELERY_RESULT_BACKEND=redis://localhost:6379/0

# Frontend URL
FRONTEND_URL=http://localhost:3000
```

### 5️⃣ Apply migrations

```bash
cd pythonbackend
python manage.py makemigrations
python manage.py migrate
```

### 6️⃣ Create superuser

```bash
python manage.py createsuperuser
```

### 7️⃣ Run server

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

### Django Built-in Authentication
* Register new users
* Login & Logout functionality
* Only logged-in users can create/edit/delete tweets

### OAuth2 (Google Login)
* Users can log in using their Google account
* Configured via `social-auth-app-django`
* Credentials stored securely using environment variables

### JWT Token Authentication
* Token-based API authentication
* Access Token Lifetime: 15 minutes
* Refresh Token Lifetime: 7 days
* Automatic token rotation enabled

### Email Verification
* Users receive verification emails after registration
* Async email processing using Celery + Redis
* 24-hour token expiry for verification links

---

## 📦 Dependencies Overview

### Authentication & OAuth2
- `social-auth-app-django==5.4.0` - OAuth2 integration
- `social-auth-storage-django==1.1.2` - OAuth2 storage backend

### JWT & REST API
- `DjangoRestFramework==3.14.0` - REST API framework
- `django-rest-framework-simplejwt==5.3.2` - JWT authentication

### Email & Async Tasks
- `celery==5.3.4` - Async task queue
- `redis==5.0.1` - Message broker
- `django-celery-beat==2.5.0` - Periodic task scheduler

### Utilities
- `python-decouple==3.8` - Environment variable management
- `requests==2.31.0` - HTTP library

---

## 🧠 Learning Outcomes

This project demonstrates:

* Django project structure and organization
* URL routing and views
* Template rendering
* Form handling and validation
* Database models and ORM
* Advanced authentication systems (OAuth2, JWT, Email verification)
* Asynchronous task processing with Celery
* REST API development
* File uploads and media handling
* Environment configuration management
* Security best practices (CSRF, CORS, secure cookies)

---

## 🚀 Future Improvements

* ❤️ Like & Comment system
* 🔔 Notifications
* 🤖 AI-based sentiment analysis on tweets
* 📊 User analytics dashboard
* 🌐 React frontend integration
* 🔐 Two-factor authentication (2FA)

---

## 🤝 Contributing

Feel free to fork this repo and submit pull requests!

---

## 📜 License

This project is open-source and available under the MIT License.

---
