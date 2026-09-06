
# 🚀 Trello Clone – Task Management API

A backend implementation of a **Trello-like project management system** built using **Python, Django, and Django REST Framework (DRF)**.

The application allows users to create boards, organize tasks into lists, assign members, and manage task workflows through RESTful APIs.

---

## 🛠️ Tech Stack

* **Python**
* **Django**
* **Django REST Framework**
* **PostgreSQL / SQLite**
* **JWT Authentication**
* **Django ORM**
* **Git & GitHub**

---

## ✨ Features

### 🔐 Authentication

* User registration
* User login
* JWT-based authentication
* Logout using token blacklisting
* Protected APIs

### 📋 Boards

* Create a board
* View boards
* Update board details
* Delete a board
* Add members to a board

### 🗂️ Lists

* Create lists inside a board
* Update lists
* Delete lists
* Arrange tasks inside lists

### ✅ Tasks / Cards

* Create tasks
* Update tasks
* Delete tasks
* Assign tasks to users
* Move tasks between lists
* Set task descriptions and due dates

### 👥 Members

* Add members to boards
* Assign members to tasks
* Manage board access

---

## 📁 Project Structure

```text
Trello/
│
├── manage.py
│
├── trello/
│   ├── settings.py
│   ├── urls.py
│   ├── asgi.py
│   └── wsgi.py
│
├── accounts/
│   ├── models.py
│   ├── serializers.py
│   ├── views.py
│   ├── urls.py
│   └── ...
│
├── boards/
│   ├── models.py
│   ├── serializers.py
│   ├── views.py
│   ├── urls.py
│   └── ...
│
├── cards/
│   ├── models.py
│   ├── serializers.py
│   ├── views.py
│   ├── urls.py
│   └── ...
│
├── requirements.txt
└── README.md
```

---

## ⚙️ Installation

### 1. Clone the repository

```bash
git clone https://github.com/your-username/trello.git
cd trello
```

### 2. Create a virtual environment

```bash
python -m venv venv
```

### 3. Activate virtual environment

**Windows:**

```bash
venv\Scripts\activate
```

**Linux / macOS:**

```bash
source venv/bin/activate
```

### 4. Install dependencies

```bash
pip install -r requirements.txt
```

---

## 🗄️ Database Setup

Run migrations:

```bash
python manage.py makemigrations
python manage.py migrate
```

Create an admin user:

```bash
python manage.py createsuperuser
```

---

## ▶️ Run the Server

```bash
python manage.py runserver
```

The API will be available at:

```text
http://127.0.0.1:8000/
```

---

## 🔑 Authentication

The API uses **JWT authentication**.

### Register

```http
POST /api/auth/signup/
```

Example:

```json
{
    "username": "john",
    "email": "john@example.com",
    "password": "password123"
}
```

### Login

```http
POST /api/auth/login/
```

Example response:

```json
{
    "access": "your-access-token",
    "refresh": "your-refresh-token"
}
```

Use the access token for protected endpoints:

```http
Authorization: Bearer <access_token>
```

---

## 🔄 API Flow

```text
User
 │
 ├── Register / Login
 │
 ▼
JWT Authentication
 │
 ▼
Board
 │
 ├── Members
 │
 ├── Lists
 │    │
 │    └── Cards / Tasks
 │
 └── Board Settings
```

---

## 🔒 Token Blacklisting

When a user logs out, the refresh token is added to a blacklist.

This prevents the logged-out refresh token from being reused.

The flow is:

```text
Login
  ↓
Access Token + Refresh Token
  ↓
API Requests
  ↓
Logout
  ↓
Refresh Token → Blacklist
  ↓
Token cannot be reused
```

---

## 🧪 API Testing

You can test the APIs using:

* Postman
* Swagger
* Django REST Framework Browsable API

Example protected request:

```http
GET /api/boards/
Authorization: Bearer <access_token>
```

---

## 📌 Future Improvements

* Drag-and-drop card ordering
* Real-time notifications
* WebSocket support
* Comments on cards
* File attachments
* Activity history
* Search and filtering
* Redis caching
* Celery background tasks
* Docker support
* API documentation with Swagger

---

## 🎯 Learning Goals

This project is designed to practice and demonstrate:

* Django project architecture
* Django REST Framework
* REST API development
* JWT authentication
* Token blacklisting
* Django ORM
* Database relationships
* Permissions and authorization
* API validation
* Backend project structure

---

## 👩‍💻 Author

**Sanskrati Patel**

Backend Developer | Python | Django | FastAPI | REST APIs

---

## ⭐ If you find this project useful

Give the repository a ⭐ on GitHub!
