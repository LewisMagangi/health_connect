# Health Connect - Project Structure Overview

## Directory Organization
```
health_connect/
├── backend/                    # Django Backend Application
│   ├── health_connect/        # Django Main Project
│   │   ├── __init__.py
│   │   ├── settings/         # Split settings
│   │   │   ├── base.py
│   │   │   ├── development.py
│   │   │   └── production.py
│   │   ├── urls.py
│   │   ├── wsgi.py
│   │   ├── asgi.py
│   │   └── celery.py        # Celery configuration
│   │
│   ├── apps/                 # Django applications
│   │   ├── users/           # User authentication and profiles
│   │   │   ├── migrations/
│   │   │   ├── templates/users/     # User-related templates
│   │   │   │   ├── login.html
│   │   │   │   ├── register.html
│   │   │   │   └── profile.html
│   │   │   ├── models/
│   │   │   │   ├── __init__.py
│   │   │   │   ├── user.py          # Base user model
│   │   │   │   ├── provider.py      # Healthcare provider model
│   │   │   │   └── patient.py       # Patient model
│   │   │   ├── views/
│   │   │   │   ├── auth.py          # Authentication views
│   │   │   │   ├── provider.py      # Provider management
│   │   │   │   └── patient.py       # Patient management
│   │   │   ├── urls.py             # URL routing
│   │   │   ├── __init__.py
│   │   │   ├── admin.py
│   │   │   ├── apps.py              # App configuration
│   │   │   ├── serializers/
│   │   │   ├── permissions.py
│   │   │   └── tasks.py
│   │   │
│   │   ├── appointments/
│   │   │   ├── migrations/
│   │   │   ├── templates/
│   │   │   ├── __init__.py
│   │   │   ├── admin.py
│   │   │   ├── apps.py              # App configuration
│   │   │   ├── forms.py
│   │   │   ├── models.py
│   │   │   ├── urls.py
│   │   │   ├── views.py
│   │   │   └── tests.py
│   │   ├── messaging/
│   │   │   ├── migrations/
│   │   │   ├── templates/
│   │   │   ├── __init__.py
│   │   │   ├── admin.py
│   │   │   ├── apps.py              # App configuration
│   │   │   ├── forms.py
│   │   │   ├── models.py
│   │   │   ├── urls.py
│   │   │   ├── views.py
│   │   │   └── tests.py
│   │   ├── doctors/
│   │   │   ├── migrations/
│   │   │   ├── templates/
│   │   │   ├── __init__.py
│   │   │   ├── admin.py
│   │   │   ├── apps.py              # App configuration
│   │   │   ├── forms.py
│   │   │   ├── models.py
│   │   │   ├── urls.py
│   │   │   ├── views.py
│   │   │   └── tests.py
│   │   ├── patients/
│   │   │   ├── migrations/
│   │   │   ├── templates/
│   │   │   ├── __init__.py
│   │   │   ├── admin.py
│   │   │   ├── apps.py              # App configuration
│   │   │   ├── forms.py
│   │   │   ├── models.py
│   │   │   ├── urls.py
│   │   │   ├── views.py
│   │   │   └── tests.py
│   │   ├── medical_records/
│   │   │   ├── migrations/
│   │   │   ├── templates/
│   │   │   ├── __init__.py
│   │   │   ├── admin.py
│   │   │   ├── apps.py              # App configuration
│   │   │   ├── forms.py
│   │   │   ├── models.py
│   │   │   ├── urls.py
│   │   │   ├── views.py
│   │   │   └── tests.py
│   │   ├── notifications/
│   │   │   ├── migrations/
│   │   │   ├── templates/
│   │   │   ├── __init__.py
│   │   │   ├── admin.py
│   │   │   ├── apps.py              # App configuration
│   │   │   ├── forms.py
│   │   │   ├── models.py
│   │   │   ├── urls.py
│   │   │   ├── views.py
│   │   │   └── tests.py
│   │   ├── lifestyle/       # Wellness and health tracking
│   │   │   ├── migrations/
│   │   │   ├── templates/lifestyle/ # Lifestyle-related templates
│   │   │   │   ├── dashboard.html
│   │   │   │   ├── tracking.html
│   │   │   │   └── plans.html
│   │   │   ├── views/
│   │   │   │   ├── __init__.py
│   │   │   │   ├── dashboard.py
│   │   │   │   └── tracking.py
│   │   │   ├── urls.py             # URL routing
│   │   │   ├── admin.py
│   │   │   ├── apps.py              # App configuration
│   │   │   ├── models.py     # Wellness plans, tracking
│   │   │   ├── serializers.py
│   │   │   ├── tasks.py      # Progress tracking
│   │   │   └── tests.py
│   │   │
│   │   ├── tools/           # Health management tools
│   │   │   ├── migrations/
│   │   │   ├── templates/tools/  # Tools templates
│   │   │   │   ├── calculator.html
│   │   │   │   └── assessment.html
│   │   │   ├── views/
│   │   │   │   ├── __init__.py
│   │   │   │   └── calculators.py
│   │   │   ├── urls.py          # URL routing
│   │   │   ├── admin.py
│   │   │   ├── apps.py              # App configuration
│   │   │   ├── models.py     # Tools and calculators
│   │   │   ├── serializers.py
│   │   │   └── tests.py
│   │   │
│   │   ├── analytics/       # Health data analytics
│   │   │   ├── migrations/
│   │   │   ├── templates/analytics/ # Analytics templates
│   │   │   │   ├── dashboard.html
│   │   │   │   ├── reports.html
│   │   │   │   └── visualizations.html
│   │   │   ├── views/
│   │   │   │   ├── __init__.py
│   │   │   │   ├── dashboard.py
│   │   │   │   └── reports.py
│   │   │   ├── urls.py            # URL routing
│   │   │   ├── admin.py
│   │   │   ├── apps.py              # App configuration
│   │   │   ├── models.py     # Analytics models
│   │   │   ├── views.py      # Data visualization
│   │   │   ├── utils.py      # Analysis helpers
│   │   │   └── tests.py
│   │   │
│   │   ├── resources/       # Educational resources
│   │   │   ├── migrations/
│   │   │   ├── templates/resources/ # Resource templates
│   │   │   │   ├── library.html
│   │   │   │   ├── article_detail.html
│   │   │   │   └── video_player.html
│   │   │   ├── static/resources/   # Resource media files
│   │   │   │   ├── videos/        # Health education videos
│   │   │   │   ├── books/         # Medical literature
│   │   │   │   ├── articles/      # Health articles
│   │   │   │   └── research/      # Research papers
│   │   │   ├── views/
│   │   │   ├── models/
│   │   │   │   ├── article.py
│   │   │   │   ├── video.py
│   │   │   │   └── document.py
│   │   │   ├── urls.py
│   │   │   └── // ...other app files...
│   │
│   ├── config/               # Configuration Files
│   │   ├── gunicorn.conf.py
│   │   ├── uwsgi.ini
│   │   ├── celery_worker.sh
│   │   └── nginx.conf
│   │
│   ├── scripts/             # Management scripts
│   │   ├── manage_db.sh
│   │   └── setup_dev_env.sh
│
├── frontend/                # React Frontend Application
│   ├── public/             # Public assets
│   │   ├── index.html      # Root HTML file
│   │   ├── favicon.ico     # Site favicon
│   │   └── assets/         # Static assets
│   │
│   ├── src/
│   │   ├── components/     # Reusable React components
│   │   │   ├── common/     # Shared components
│   │   │   ├── layout/     # Layout components
│   │   │   └── forms/      # Form components
│   │   │
│   │   ├── pages/         # Page components
│   │   │   ├── auth/       # Authentication pages
│   │   │   ├── dashboard/  # Dashboard views
│   │   │   └── profile/    # Profile pages
│   │   │
│   │   ├── services/      # API integration
│   │   │   ├── api.js      # API client setup
│   │   │   └── endpoints/  # API endpoint modules
│   │   │
│   │   ├── styles/        # CSS styles
│   │   │   ├── global.css  # Global styles
│   │   │   └── components/ # Component-specific styles
│   │   │
│   │   ├── hooks/         # Custom React hooks
│   │   ├── context/       # React context providers
│   │   ├── utils/         # Utility functions
│   │   ├── App.jsx        # Root React component
│   │   └── index.jsx      # Entry point
│   │
│   ├── package.json       # npm dependencies
│   ├── vite.config.js     # Vite configuration
│   └── tsconfig.json      # TypeScript configuration
│
├── docker/                 # Docker configuration
│   ├── Dockerfile.backend
│   ├── Dockerfile.frontend
│   └── docker-compose.yml
│
├── logs/                   # Application logs
│   ├── audit_logs/        # Security and compliance audit logs
│   │   ├── activity/      # User activity logs
│   │   └── system/        # System-level audit logs
│   ├── django_logs/       # Django application logs
│   │   ├── debug.log      # Development debugging
│   │   ├── info.log       # General information
│   │   └── errors.log     # Application errors
│   └── error_logs/        # Detailed error tracking
│       ├── backend/       # Backend service errors
│       ├── frontend/      # Frontend error logs
│       └── system/        # System-level errors
│
├── requirements/          # Split requirements
│   ├── base.txt
│   ├── development.txt
│   └── production.txt
│
├── .env.example          # Environment variables template
├── .gitignore
└── README.md
```

## Key Components Description

### Backend Structure
- **health_connect/**: Core Django configuration
  - Settings split by environment
  - Celery configuration
  - ASGI/WSGI setup

### Frontend Structure (New)
- **React SPA**
  - Component-based architecture
  - State management
  - API integration services

### Configuration
- **Docker**: Containerization for all services
- **Nginx**: Reverse proxy configuration
- **Celery**: Async task processing

### Logging
- Centralized logging for all services
- Separate logs for Django, Celery, and Nginx

### Applications (`apps/`)
- **users**: Consolidated user management system
  - Authentication and authorization
  - Provider profiles and credentials
  - Patient profiles and records
  - Role-based permissions
- **appointments**: Scheduling and appointment management
- **messaging**: Internal communication and chat system
- **doctors**: Doctor-specific functionality and specialization management
- **patients**: Patient-specific features and medical history
- **medical_records**: Medical documentation and record keeping
- **notifications**: Email, SMS, and in-app notification system
- **lifestyle**: Wellness and health tracking
- **tools**: Health management tools
- **analytics**: Health data analytics
- **resources**: Educational content management

### Configuration (`health_connect/`)
- Settings split by environment
- URL routing configuration
- WSGI/ASGI server settings

### Static Files (`static/`)
- CSS stylesheets
- JavaScript files
- Image assets

### Templates (`templates/`)
- Base templates and layouts
- Application-specific templates
- Reusable components

### Development Tools
- Docker configuration for containerization
- Environment variable management
- Deployment scripts

## Standard App Structure
Every Django app should include:
- `migrations/` - Database migrations
- `templates/<app_name>/` - App-specific templates
- `views/` - View logic (function or class-based)
- `urls.py` - URL routing
- `models.py` - Database models
- `admin.py` - Admin interface
- `apps.py` - App configuration
- `serializers.py` - DRF serializers (if API)
- `tests.py` - Unit tests
- `forms.py` - Form definitions (if needed)

