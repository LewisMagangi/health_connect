# Core User Models

## User
Base user model that extends Django's AbstractUser:
- Authentication Fields (Required)
  - username: string (unique)
  - email: string (unique, verified)
  - password: string (hashed)
  - last_login: datetime
  - date_joined: datetime

- Personal Information (Required)
  - first_name: string
  - last_name: string
  - profile: OneToOne to Profile
  - user_type: enum[PATIENT, PROVIDER, ADMIN, STAFF]

- Account Status
  - is_active: boolean
  - is_staff: boolean
  - is_superuser: boolean
  - status: enum[ACTIVE, INACTIVE, SUSPENDED, PENDING_VERIFICATION]

- Security Fields
  - email_verified: boolean
  - phone_verified: boolean
  - two_factor_enabled: boolean
  - account_locked: boolean
  - login_attempts: integer

- Extended Models
  * If user_type == PROVIDER:
    - medical_professional: OneToOne to MedicalProfessional
  * If user_type == PATIENT:
    - patient: OneToOne to Patient

## AbstractUser Extensions
Base classes for specific user types:

### AbstractProvider
Extended by MedicalProfessional:
- Base provider functionality
- License verification methods
- Scheduling capabilities
- Service management

### AbstractPatient
Extended by Patient:
- Health record access
- Appointment management
- Wellness plan tracking
- Medical history

## Common Functionality
- Authentication methods
- Password management
- Profile updates
- Security checks
- Access control

## Indexes
- username: unique
- email: unique
- user_type: index
- status: index

## Related Models
- Profile (OneToOne)
- AccountSecurity (OneToOne)
- UserConsent (OneToMany)
- Integration (OneToOne)
