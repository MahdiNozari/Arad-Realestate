<<<<<<< HEAD
# Real Estate Management System

A Django-based Real Estate Management System designed to streamline property management, user accounts, and real estate contracts.
The project is structured into modular apps for better maintainability: Accounts, Contracts, Requests, and Home.

---

## 🚀 Features

* User Authentication & Management (Accounts App)

  * Registration, login, logout
  * Profile management (basic user info, contact details, etc.)
  * Role-based permissions (staff/admin vs. regular users)
  * Password reset and security features

* Contracts Management (Contracts App)

  * Create, edit, and delete contracts
  * Store contract documents (PDFs, images, etc.)
  * Associate contracts with users and properties
  * Track contract status (draft, active, expired)

* Property Requests (Requests App)

  * Users can request properties (rent, buy, or sell)
  * Agents/admins can review, approve, or reject requests
  * Requests linked with user accounts for tracking
  * Request history for auditing purposes

* Home & Dashboard (Home App)

  * Public landing pages (homepage, about, contact)
  * Central dashboard for authenticated users
  * Quick navigation to contracts, requests, and account details
  * UI built with Bootstrap v4 RTL for responsive design

---

## 🛠️ Tech Stack

* Backend: Django (Python)
* Frontend: Django Templates + Bootstrap 4 (RTL support)  
* Database: PostgreSQL
* Static Files: CSS, JS, images managed by Django staticfiles
* Media Files: User-uploaded files (contracts, profile pictures, etc.)

---

## 📂 Project Structure


realestate/
├── accounts/        # Authentication and user management
│   ├── models.py    # User profiles, roles, authentication helpers
│   ├── views.py     # Login, signup, profile, password reset
│   ├── urls.py      # Auth-related routes
│
├── contracts/       # Property contracts management
│   ├── models.py    # Contract model with user and property references
│   ├── views.py     # CRUD for contracts
│   ├── urls.py      # Contracts routes
│
├── requests/        # User property requests
│   ├── models.py    # Request model linked to user
│   ├── views.py     # Create & manage requests
│   ├── urls.py      # Requests routes
│
├── home/            # Landing pages & dashboards
│   ├── views.py     # Homepage, dashboard, static pages
│   ├── urls.py      # Home routes
│
├── templates/       # Global templates for all apps
├── static/          # CSS, JS, images
├── media/           # Uploaded files
├── realestate/      # Project settings, main URLs, WSGI/ASGI
├── manage.py        # Django management script
└── requirements.txt # Python dependencies

---

## ⚙️ Installation & Setup

1. Clone the repository

   bash
   git clone https://github.com/MahdiNozari/Arad-Realestate.git
   cd realestate/realestate
   
2. Create and activate a virtual environment

   bash
   python -m venv venv
   source venv/bin/activate   # Linux/Mac
   venv\Scripts\activate      # Windows
   
3. Install dependencies

   bash
   pip install -r requirements.txt
   
4. Run migrations

   bash
   python manage.py migrate
   
5. Create a superuser

   bash
   python manage.py createsuperuser
   
6. Start the development server

   bash
   python manage.py runserver
   
7. Visit the app at http://127.0.0.1:8000/

---

## 🔑 Environment Variables

Configure sensitive settings using .env:

env
DEBUG=True
ALLOWED_HOSTS=localhost,127.0.0.1

---


## 📦 Deployment

* Set DEBUG=False in production

* Collect static files:

  bash
  python manage.py collectstatic
  
* Use a WSGI/ASGI server
=======
czczs
>>>>>>> 76054195eac44ea01481f4b81bbfb7a81a568a0e
