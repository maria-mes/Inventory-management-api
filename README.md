# Inventory-management-api

## 📌 Overview
A Django REST Framework API for managing inventory items and users.  
Supports CRUD operations, authentication, filtering, inventory tracking, and deployment.  
Built as part of the ALX Backend Engineering Capstone.

---

## ⚙️ Features
- **Inventory CRUD**: Create, read, update, delete items with attributes:
  - Name, Description, Quantity, Price, Category, Date Added, Last Updated
- **User CRUD**: Manage users (Username, Email, Password)
- **Ownership**: Authenticated users manage their own items
- **Comments**: Add notes to products
- **Search & Filtering**: Query by name, description, category, tags
- **Inventory Change Tracking**: Logs restocks/sales with history
- **Authentication**: JWT‑based secure endpoints
- **Documentation**: Swagger/OpenAPI auto‑generated
- **Tests**: Unit and integration tests for validator compliance
- **Pagination & Sorting**: Page results, sort by Name, Quantity, Price, Date Added

---

## 🛠️ Tech Stack
- Django
- Django REST Framework
- PostgreSQL (Heroku) / SQLite (local dev)
- drf‑yasg (Swagger docs)
- django‑filter
- simplejwt
- gunicorn

---

## 📂 Project Structure

inventory_api/
├── inventory/        # Core app: models, views, serializers, tests
├── inventory_api/    # Project settings, urls
├── manage.py
├── requirements.txt
└── README.md


---

## 🚀 Getting Started

### 1. Clone the repo
bash
git clone https://github.com/maria-mes/Inventory-management-api.git
cd Inventory-management-api

### 2. Install dependencies
pip install -r requirements.txt

### 3. Run migrations
python manage.py migrate

### 4. start server
python manage.py runserver
Visit: http://127.0.0.1:8000/api/

🔐 Authentication
Obtain token:

Code
POST /api/token/
Refresh token:

Code
POST /api/token/refresh/
Include the token in headers:

Code
Authorization: Bearer <your_token>
📖 API Documentation
Swagger UI: /swagger/

Redoc: /redoc/

🧪 Running Tests
bash
python manage.py test
🔄 Inventory Change Tracking
ChangeLog model records restocks/sales:

Product, User, Change Type, Quantity Changed, Timestamp

Endpoint: /api/changes/ to view history


## 🚀 Deployment (Heroku)

1. Install Heroku CLI and log in.
2. Create app: heroku create inventory-api-mara
3. Add Postgres: heroku addons:create heroku-postgresql:hobby-dev
4. Push code: git push heroku main
5. Run migrations: heroku run python manage.py migrate
6. Access API at: https://inventory-api-mara.herokuapp.com/api/
