# Health Connect

A Django-based healthcare platform. For detailed project overview, see [docs/overview.md](docs/overview.md).

## Project Structure
```
health_connect/
├── docs/               # Project documentation
├── health_connect/     # Django project settings
├── manage.py          # Django management script
├── requirements.txt   # Project dependencies
└── README.md         # This file (project documentation)
```

## Setup Instructions

1. Clone the repository:
```bash
git clone <repository-url>
cd health_connect
```

2. Create and activate virtual environment:
```bash
python -m venv health_connect_venv
health_connect_venv\Scripts\activate  # On Windows
# OR
source health_connect_venv/bin/activate  # On Unix/MacOS
```

3. Upgrade pip and install dependencies:
```bash
python -m pip install --upgrade pip
pip install -r requirements.txt
```

4. Initialize the Django project:
```bash
django-admin startproject health_connect .  # Note the dot!
```

5. Run migrations:
```bash
python manage.py migrate
```

6. Start development server:
```bash
python manage.py runserver
```

## Development

The application will be available at http://localhost:8000

## License
This project is licensed under the MIT License.
