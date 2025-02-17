# Health Connect - Current Project Structure

## Directory Structure as of 2025-02-17 08:46:48
```
health_connect/
├── health_connect/
│   ├── README.md
│   ├── db.sqlite3
│   ├── manage.py
│   ├── requirements.txt
│   ├── update_structure.py
│   ├── urls.py
│   ├── apps/
│   │   ├── accounts/
│   │   │   ├── __init__.py
│   │   │   ├── admin.py
│   │   │   ├── apps.py
│   │   │   ├── forms.py
│   │   │   ├── models.py
│   │   │   ├── tests.py
│   │   │   ├── urls.py
│   │   │   ├── views.py
│   │   │   ├── migrations/
│   │   │   │   ├── __init__.py
│   │   │   ├── templates/
│   │   │   │   ├── accounts/
│   │   │   │   │   ├── complete_profile.html
│   │   │   │   │   ├── login.html
│   │   │   │   │   ├── register.html
│   │   │   │   │   ├── register_step_one.html
│   │   │   │   │   ├── register_step_two.html
│   │   ├── analytics/
│   │   │   ├── __init__.py
│   │   │   ├── admin.py
│   │   │   ├── apps.py
│   │   │   ├── models.py
│   │   │   ├── tests.py
│   │   │   ├── views.py
│   │   │   ├── migrations/
│   │   │   │   ├── 0001_initial.py
│   │   │   │   ├── __init__.py
│   │   ├── appointments/
│   │   │   ├── __init__.py
│   │   │   ├── admin.py
│   │   │   ├── apps.py
│   │   │   ├── models.py
│   │   │   ├── tests.py
│   │   │   ├── urls.py
│   │   │   ├── views.py
│   │   │   ├── migrations/
│   │   │   │   ├── 0001_initial.py
│   │   │   │   ├── __init__.py
│   │   ├── billing/
│   │   │   ├── __init__.py
│   │   │   ├── admin.py
│   │   │   ├── apps.py
│   │   │   ├── models.py
│   │   │   ├── tests.py
│   │   │   ├── urls.py
│   │   │   ├── views.py
│   │   │   ├── migrations/
│   │   │   │   ├── 0001_initial.py
│   │   │   │   ├── __init__.py
│   │   ├── communications/
│   │   │   ├── __init__.py
│   │   │   ├── admin.py
│   │   │   ├── apps.py
│   │   │   ├── models.py
│   │   │   ├── tests.py
│   │   │   ├── urls.py
│   │   │   ├── views.py
│   │   │   ├── migrations/
│   │   │   │   ├── 0001_initial.py
│   │   │   │   ├── __init__.py
│   │   ├── dashboard/
│   │   │   ├── __init__.py
│   │   │   ├── apps.py
│   │   │   ├── urls.py
│   │   │   ├── views.py
│   │   ├── lifestyle/
│   │   │   ├── __init__.py
│   │   │   ├── admin.py
│   │   │   ├── apps.py
│   │   │   ├── models.py
│   │   │   ├── tests.py
│   │   │   ├── views.py
│   │   │   ├── migrations/
│   │   │   │   ├── 0001_initial.py
│   │   │   │   ├── __init__.py
│   │   ├── medicalproffesionals/
│   │   │   ├── __init__.py
│   │   │   ├── admin.py
│   │   │   ├── apps.py
│   │   │   ├── models.py
│   │   │   ├── tests.py
│   │   │   ├── views.py
│   │   │   ├── migrations/
│   │   │   │   ├── 0001_initial.py
│   │   │   │   ├── __init__.py
│   │   ├── medicalrecords/
│   │   │   ├── __init__.py
│   │   │   ├── admin.py
│   │   │   ├── apps.py
│   │   │   ├── models.py
│   │   │   ├── tests.py
│   │   │   ├── urls.py
│   │   │   ├── views.py
│   │   │   ├── migrations/
│   │   │   │   ├── 0001_initial.py
│   │   │   │   ├── __init__.py
│   │   ├── medical_records/
│   │   │   ├── models.py
│   │   ├── resources/
│   │   │   ├── __init__.py
│   │   │   ├── admin.py
│   │   │   ├── apps.py
│   │   │   ├── models.py
│   │   │   ├── tests.py
│   │   │   ├── views.py
│   │   │   ├── migrations/
│   │   │   │   ├── 0001_initial.py
│   │   │   │   ├── __init__.py
│   │   ├── tools/
│   │   │   ├── __init__.py
│   │   │   ├── admin.py
│   │   │   ├── apps.py
│   │   │   ├── models.py
│   │   │   ├── tests.py
│   │   │   ├── views.py
│   │   │   ├── migrations/
│   │   │   │   ├── 0001_initial.py
│   │   │   │   ├── __init__.py
│   │   ├── users/
│   │   │   ├── __init__.py
│   │   │   ├── admin.py
│   │   │   ├── apps.py
│   │   │   ├── models.py
│   │   │   ├── signals.py
│   │   │   ├── tests.py
│   │   │   ├── views.py
│   │   │   ├── migrations/
│   │   │   │   ├── 0001_initial.py
│   │   │   │   ├── __init__.py
│   ├── core/
│   │   ├── urls.py
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
│   │   │   │   │   ├── diagram.md
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
│   │   │   ├── login.css
│   │   │   ├── main.css
│   ├── templates/
│   │   ├── base.html
│   │   ├── home.html
│   │   ├── accounts/
│   │   │   ├── login.html
│   │   ├── appointments/
│   │   │   ├── schedule.html
│   │   ├── billing/
│   │   │   ├── invoice_detail.html
│   │   │   ├── invoice_list.html
│   │   ├── dashboard/
│   │   │   ├── admin_dashboard.html
│   │   │   ├── doctor_dashboard.html
│   │   │   ├── patient_dashboard.html
│   │   ├── medicalrecords/
│   │   │   ├── view.html
│   │   ├── messages/
│   │   │   ├── compose.html
│   │   │   ├── inbox.html
```
