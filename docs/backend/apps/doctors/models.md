# Healthcare Providers Models

## Common Fields
Fields shared across all models:
- Audit Information (Auto-generated)
  - created_at: timestamp
  - updated_at: timestamp
  - created_by: foreign key to User
  - updated_by: foreign key to User

## Specialization Model
Medical specialties and subspecialties management:
- Basic Information
  - name: string (required)
  - description: text (required)
  - parent_specialty: foreign key to self (optional)

## HospitalAffiliation Model
Hospital and clinic affiliations:
- Basic Information
  - name: string (required)
  - address: foreign key to Address (required)
  - affiliation_type: enum[PRIMARY, SECONDARY, VISITING] (required)
  - start_date: date (required)
  - end_date: date (optional)
  - is_current: boolean (computed)

## MedicalProfessional Model
Core model for all healthcare providers:
- Provider Information (All Required)
  - provider_type: enum[DOCTOR, NURSE, THERAPIST]
  - license_number: string (unique)
  - specializations: ManyToMany to Specialization
  - qualifications: json
  - years_of_experience: integer
  - practicing_since: date

- Status and Availability
  - is_active: boolean (required, default: true)
  - availability_status: enum[AVAILABLE, UNAVAILABLE, ON_LEAVE, LIMITED]
  - schedule_calendar: foreign key to Calendar (optional)
  - service_locations: ManyToMany to Address
  - languages_spoken: array of language codes

- Practice Details
  - hospital_affiliations: ManyToMany to HospitalAffiliation
  - office_hours: json (required)
  - consultation_fee: decimal (required)
  - available_for_telemedicine: boolean (optional)

- Professional Profile
  - bio: text (optional)
  - achievements: json (optional)
  - research_publications: json (optional)
  - References to User/Profile models:
    * profile_picture: from Profile
    * contact_info: from Profile
    * emergency_contacts: from Profile

- Verification (All Required)
  - license_verified: boolean
  - verification_documents: json
  - verification_status: enum[PENDING, VERIFIED, REJECTED]

- Role-specific Information
  - role_specific_details: json (optional)
    * For doctors: board certifications, subspecialties
    * For nurses: specialization areas, certifications
    * For therapists: therapy types, treatment methods

## Relationships
- MedicalProfessional -> User (OneToOne)
- MedicalProfessional -> HospitalAffiliation (ManyToMany)
- MedicalProfessional -> Specialization (ManyToMany)
- MedicalProfessional -> Address (ManyToMany through ServiceLocation)
- HospitalAffiliation -> Address (ForeignKey)

## Indexing
- MedicalProfessional.license_number: unique index
- MedicalProfessional.provider_type: index
- MedicalProfessional.is_active: index
- HospitalAffiliation.name: index
