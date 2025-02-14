# Health Connect - Current Project Structure

## Directory Structure as of 2025-02-14 16:33:49
```
health_connect/
├── health_connect/
│   ├── README.md
│   ├── db.sqlite3
│   ├── manage.py
│   ├── requirements.txt
│   ├── update_structure.py
│   ├── apps/
│   │   ├── accounts/
│   │   │   ├── __init__.py
│   │   │   ├── admin.py
│   │   │   ├── apps.py
│   │   │   ├── models.py
│   │   │   ├── tests.py
│   │   │   ├── views.py
│   │   │   ├── migrations/
│   │   │   │   ├── __init__.py
│   │   ├── analytics/
│   │   │   ├── __init__.py
│   │   │   ├── admin.py
│   │   │   ├── apps.py
│   │   │   ├── models.py
│   │   │   ├── tests.py
│   │   │   ├── views.py
│   │   │   ├── migrations/
│   │   │   │   ├── __init__.py
│   │   ├── appointments/
│   │   │   ├── __init__.py
│   │   │   ├── admin.py
│   │   │   ├── apps.py
│   │   │   ├── models.py
│   │   │   ├── tests.py
│   │   │   ├── views.py
│   │   │   ├── migrations/
│   │   │   │   ├── __init__.py
│   │   ├── billing/
│   │   │   ├── __init__.py
│   │   │   ├── admin.py
│   │   │   ├── apps.py
│   │   │   ├── models.py
│   │   │   ├── tests.py
│   │   │   ├── views.py
│   │   │   ├── migrations/
│   │   │   │   ├── __init__.py
│   │   ├── communications/
│   │   │   ├── __init__.py
│   │   │   ├── admin.py
│   │   │   ├── apps.py
│   │   │   ├── models.py
│   │   │   ├── tests.py
│   │   │   ├── views.py
│   │   │   ├── migrations/
│   │   │   │   ├── __init__.py
│   │   ├── lifestyle/
│   │   │   ├── __init__.py
│   │   │   ├── admin.py
│   │   │   ├── apps.py
│   │   │   ├── models.py
│   │   │   ├── tests.py
│   │   │   ├── views.py
│   │   │   ├── migrations/
│   │   │   │   ├── __init__.py
│   │   ├── medicalproffesionals/
│   │   │   ├── __init__.py
│   │   │   ├── admin.py
│   │   │   ├── apps.py
│   │   │   ├── models.py
│   │   │   ├── tests.py
│   │   │   ├── views.py
│   │   │   ├── migrations/
│   │   │   │   ├── __init__.py
│   │   ├── medicalrecords/
│   │   │   ├── __init__.py
│   │   │   ├── admin.py
│   │   │   ├── apps.py
│   │   │   ├── models.py
│   │   │   ├── tests.py
│   │   │   ├── views.py
│   │   │   ├── migrations/
│   │   │   │   ├── __init__.py
│   │   ├── resources/
│   │   │   ├── __init__.py
│   │   │   ├── admin.py
│   │   │   ├── apps.py
│   │   │   ├── models.py
│   │   │   ├── tests.py
│   │   │   ├── views.py
│   │   │   ├── migrations/
│   │   │   │   ├── __init__.py
│   │   ├── tools/
│   │   │   ├── __init__.py
│   │   │   ├── admin.py
│   │   │   ├── apps.py
│   │   │   ├── models.py
│   │   │   ├── tests.py
│   │   │   ├── views.py
│   │   │   ├── migrations/
│   │   │   │   ├── __init__.py
│   │   ├── users/
│   │   │   ├── __init__.py
│   │   │   ├── admin.py
│   │   │   ├── apps.py
│   │   │   ├── models.py
│   │   │   ├── tests.py
│   │   │   ├── views.py
│   │   │   ├── migrations/
│   │   │   │   ├── __init__.py
│   ├── core/
│   │   ├── views.py
│   ├── docs/
│   │   ├── current_project_structure.md
│   │   ├── overview.md
│   │   ├── project_structure.md
│   │   ├── structure.md
│   │   ├── tech_stack.md
│   │   ├── backend/
│   │   │   ├── apps/
│   │   │   │   ├── README.md
│   │   │   │   ├── accounts/
│   │   │   │   │   ├── models.md
│   │   │   │   ├── analytics/
│   │   │   │   │   ├── models.md
│   │   │   │   ├── appointments/
│   │   │   │   │   ├── models.md
│   │   │   │   ├── architecture/
│   │   │   │   │   ├── model_interactions.md
│   │   │   │   │   ├── model_relationships.md
│   │   │   │   ├── billing/
│   │   │   │   │   ├── models.md
│   │   │   │   ├── communications/
│   │   │   │   │   ├── models.md
│   │   │   │   ├── lifestyle/
│   │   │   │   │   ├── models.md
│   │   │   │   ├── medicalproffesionals/
│   │   │   │   │   ├── models.md
│   │   │   │   ├── medical_records/
│   │   │   │   │   ├── models.md
│   │   │   │   ├── prescriptions/
│   │   │   │   │   ├── models.md
│   │   │   │   ├── settings/
│   │   │   │   │   ├── models.md
│   │   │   │   ├── tools/
│   │   │   │   │   ├── models.md
│   │   │   │   ├── users/
│   │   │   │   │   ├── models/
│   │   │   │   │   │   ├── address.md
│   │   │   │   │   │   ├── communication_preferences.md
│   │   │   │   │   │   ├── consent.md
│   │   │   │   │   │   ├── medical_professional.md
│   │   │   │   │   │   ├── user.md
│   │   │   ├── mvp/
│   │   │   │   ├── IMPLEMENTATION.md
│   │   │   │   ├── README.md
│   │   │   │   ├── core_models.md
│   │   ├── frontend/
│   │   │   ├── architecture.md
│   │   ├── infrastructure/
│   │   │   ├── README.md
│   │   │   ├── audit_logs.md
│   ├── health_connect/
│   │   ├── __init__.py
│   │   ├── asgi.py
│   │   ├── settings.py
│   │   ├── urls.py
│   │   ├── views.py
│   │   ├── wsgi.py
│   ├── static/
│   │   ├── css/
│   │   │   ├── main.css
│   ├── templates/
│   │   ├── base.html
│   │   ├── home.html
```
