# MVP Core Models Specification

## Authentication Models

### User
Essential attributes:
- username (unique)
- email (unique)
- password (hashed)
- first_name
- last_name
- user_type: PATIENT or PROVIDER
- is_active
- created_at
- updated_at

### Profile
Basic profile data:
- user (link to User)
- date_of_birth
- phone_number
- address
- emergency_contact
- created_at
- updated_at

### MedicalProfessional
Core provider details:
- user (link to User)
- license_number (unique)
- specialization
- years_of_experience
- is_active
- created_at
- updated_at

## Care Management

### Appointment
Essential scheduling:
- patient (link to User)
- provider (link to MedicalProfessional)
- date_time
- status: SCHEDULED, COMPLETED, CANCELLED
- appointment_type: IN_PERSON, VIRTUAL
- notes (optional)
- created_at
- updated_at

### MedicalRecord
Basic patient history:
- patient (link to User)
- medical_history
- allergies (optional)
- current_medications (optional)
- created_at
- updated_at

### Consultation
Basic visit records:
- patient (link to User)
- provider (link to MedicalProfessional)
- date
- symptoms
- diagnosis
- treatment
- notes (optional)
- created_at
- updated_at

## Communication

### Message
Simple messaging:
- sender (link to User)
- recipient (link to User)
- content
- read_status
- created_at

## Required Indexes
- User: email, username
- MedicalProfessional: license_number
- Appointment: date_time, provider
- MedicalRecord: patient
- Message: recipient + read_status

## Notes
1. All models include audit timestamps
2. All foreign key relationships are required
3. Only essential fields included for MVP
4. Simple data types (string, text, datetime, boolean)
5. No complex JSON fields for MVP phase
