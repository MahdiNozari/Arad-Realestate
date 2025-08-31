# 🏠 Real Estate Management System

A comprehensive Django-based platform designed to streamline property management operations, user account management, and real estate contract handling. The system is modularly designed for scalability and maintainability.

![Django](https://img.shields.io/badge/Django-4.2-green)
![Bootstrap](https://img.shields.io/badge/Bootstrap-4.6-blue)
![PostgreSQL](https://img.shields.io/badge/PostgreSQL-13-blueviolet)

## ✨ Key Features

### 👥 User Authentication & Management
- **Role-based access control** (Admin, Staff, Client)
- **User registration & profile management** with contact details
- **Secure authentication** with password reset functionality
- **Personalized dashboards** based on user roles

### 📑 Contracts Management
- **Digital contract creation** and management
- **Document storage** for PDFs and images
- **Contract status tracking** (Draft, Active, Expired)
- **User-property contract associations**

### 🏢 Property Requests System
- **Multi-type property requests** (Rent, Buy, Sell)
- **Request workflow management** (Submitted, In Review, Approved, Rejected)
- **Audit trail** for all request modifications
- **Client-agent communication** platform

### 📊 Dashboard & Analytics
- **Interactive dashboard** with property statistics
- **Quick navigation** to key system features
- **Responsive design** with Bootstrap 4 RTL support

## 🏗️ System Architecture

```
realestate/
├── accounts/          # User authentication & management
│   ├── models.py      # Custom User model, Profile, Roles
│   ├── views.py       # Auth views, profile management
│   ├── forms.py       # User registration & profile forms
│   └── urls.py        # Authentication endpoints
├── contracts/         # Contract management system
│   ├── models.py      # Contract model with status tracking
│   ├── views.py       # CRUD operations for contracts
│   ├── admin.py       # Admin interface configuration
│   └── urls.py        # Contract-related routes
├── requests/          # Property request handling
│   ├── models.py      # Request model with state management
│   ├── views.py       # Request creation & management
│   ├── utils.py       # Request processing utilities
│   └── urls.py        # Request API endpoints
├── home/              # Main dashboard & landing pages
│   ├── views.py       # Homepage, dashboard, static pages
│   ├── context.py     # Context processors for dashboard data
│   └── urls.py        # Public & dashboard routes
├── templates/         # Global template directory
│   ├── base.html      # Main template structure
│   ├── dashboard/     # Role-specific dashboards
│   └── includes/      # Reusable template components
├── static/            # CSS, JavaScript, images
│   ├── css/           # Custom stylesheets
│   ├── js/            # Interactive functionality
│   └── images/        # App imagery and icons
├── media/             # User-uploaded files
├── realestate/        # Project configuration
│   ├── settings/      # Environment-specific settings
│   │   ├── base.py    # Common settings
│   │   ├── dev.py     # Development settings
│   │   └── prod.py    # Production settings
│   ├── urls.py        # Main URL routing
│   └── wsgi.py        # WSGI application entry point
└── manage.py          # Django management script
```

## 🛠️ Technology Stack

| Component           | Technology |
|---------------------|------------|
| **Backend Framework** | Django |
| **Database**        | PostgreSQL |

## 📦 Installation Guide

### Prerequisites
- Python 3.9+
- PostgreSQL 12+
- pip 20+

### Local Development Setup

1. **Clone the repository**
   ```bash
   git clone https://github.com/MahdiNozari/Arad-Realestate.git
   cd Arad-Realestate
   ```

2. **Create and activate virtual environment**
   ```bash
   python -m venv venv
   source venv/bin/activate  # Linux/MacOS
   # or
   venv\Scripts\activate     # Windows
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Environment configuration**


5. **Database setup**
   ```bash
   python manage.py migrate
   ```

6. **Create superuser**
   ```bash
   python manage.py createsuperuser
   ```

7. **Run development server**
   ```bash
   python manage.py runserver
   ```

8. **Access the application**
   ```
   http://localhost:8000
   Admin panel: http://localhost:8000/admin
   ```

## ⚙️ Configuration

### Environment Variables

Create a `.env` file in the project root:

```ini
# Django Settings
DEBUG=True
ALLOWED_HOSTS=localhost,127.0.0.1

# Database Configuration
DB_NAME=
DB_USER=
DB_PASSWORD=
DB_HOST=
DB_PORT=

# Email Configuration
EMAIL_BACKEND=django.core.mail.backends.smtp.EmailBackend
EMAIL_HOST=smtp.gmail.com
EMAIL_PORT=587
EMAIL_USE_TLS=True
EMAIL_HOST_USER=your-email@gmail.com
EMAIL_HOST_PASSWORD=your-app-password

# File Storage
USE_S3=False
AWS_ACCESS_KEY_ID=your-aws-key
AWS_SECRET_ACCESS_KEY=your-aws-secret
AWS_STORAGE_BUCKET_NAME=your-bucket-name
```

### Database Configuration

The system uses PostgreSQL by default. Update your DATABASES setting:

```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': os.getenv('DB_NAME'),
        'USER': os.getenv('DB_USER'),
        'PASSWORD': os.getenv('DB_PASSWORD'),
        'HOST': os.getenv('DB_HOST', 'localhost'),
        'PORT': os.getenv('DB_PORT', '5432'),
    }
}
```

## 👥 User Roles & Permissions

| Role | Permissions |
|------|-------------|
| **Admin** | Full system access, user management, all CRUD operations |
| **Staff/Agent** | Property and contract management, client request handling |
| **Client** | Property requests, view own contracts, profile management |

## 🚀 Deployment

### Production Setup with Docker

1. **Build and run with Docker Compose**
   ```bash
   docker-compose -f docker-compose.prod.yml up --build
   ```

2. **Collect static files**
   ```bash
   docker-compose exec web python manage.py collectstatic --noinput
   ```

3. **Run migrations**
   ```bash
   docker-compose exec web python manage.py migrate
   ```

### Manual Deployment

1. **Set up production environment variables**
   ```bash
   export DEBUG=False
   export ALLOWED_HOSTS=your-domain.com,www.your-domain.com
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements/production.txt
   ```

3. **Collect static files**
   ```bash
   python manage.py collectstatic
   ```

4. **Configure web server (Nginx example)**
   ```nginx
   server {
       listen 80;
       server_name your-domain.com www.your-domain.com;
       
       location /static/ {
           alias /path/to/your/staticfiles/;
       }
       
       location /media/ {
           alias /path/to/your/mediafiles/;
       }
       
       location / {
           proxy_pass http://localhost:8000;
           proxy_set_header Host $host;
           proxy_set_header X-Real-IP $remote_addr;
       }
   }
   ```

5. **Run with Gunicorn**
   ```bash
   gunicorn --workers 3 realestate.wsgi:application
   ```

## 🤝 Contributing

We welcome contributions! Please follow these steps:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

### Development Guidelines

- Follow PEP 8 style guide for Python code
- Write tests for new functionality
- Update documentation for new features
- Use descriptive commit messages

## 🧪 Testing

Run the test suite to ensure everything works correctly:

```bash
# Run all tests
python manage.py test

# Run specific app tests
python manage.py test accounts

# Run with coverage report
coverage run manage.py test
coverage report
```

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🆘 Support

If you encounter any problems or have questions:
2. Search existing [issues](https://github.com/MahdiNozari/Arad-Realestate/issues)
3. Create a new issue with detailed information


