# Medical Professional Models

## MedicalProfessional (Base Model)
Common fields for all healthcare providers:
- Base Information
  - id: unique identifier (UUID)
  - user: OneToOne to User
  - provider_type: enum[DOCTOR, NURSE, THERAPIST, SPECIALIST]
  - license_number: string (required)
  - practicing_since: date (required)
  - years_of_experience: integer (computed)
  - is_active: boolean
  
- Professional Details
  - primary_specialization: string (required)
  - additional_specializations: array
  - qualifications: array
  - certifications: array
  - languages_spoken: array
  
- Verification
  - license_verified: boolean
  - verification_status: enum[PENDING, VERIFIED, REJECTED]
  - verification_documents: array
  - last_verification_date: datetime
  
- Practice Information
  - practice_locations: ManyToMany to Address
  - service_areas: array
  - accepts_insurance: boolean
  - available_for_telemedicine: boolean

## Doctor (Extends MedicalProfessional)
Doctor-specific attributes:
- Medical Details
  - medical_school: string
  - residency_location: string
  - board_certifications: array
  - hospital_affiliations: array
  
- Practice Details
  - consultation_types: array[GENERAL, SPECIALIST, SURGERY]
  - surgical_privileges: boolean
  - teaching_status: enum[NONE, RESIDENT, ATTENDING, PROFESSOR]

## Specialist (Extends MedicalProfessional)
Specialist-specific attributes:
- Specialty Details
  - sub_specialties: array
  - specialty_certifications: array
  - specialized_procedures: array
  
- Research & Publications
  - research_areas: array
  - publications: array
  - clinical_trials: array

## Nurse (Extends MedicalProfessional)
Nurse-specific attributes:
- Nursing Details
  - nursing_level: enum[RN, NP, CNS]
  - clinical_focus_areas: array
  - specialized_care_units: array

## Therapist (Extends MedicalProfessional)
Therapist-specific attributes:
- Therapy Details
  - therapy_types: array
  - treatment_approaches: array
  - patient_age_groups: array

## Common Related Models

### ProfessionalSchedule
Scheduling and availability:
- Base Fields
  - professional: ForeignKey to MedicalProfessional
  - location: ForeignKey to Address
  - schedule_type: enum[REGULAR, ON_CALL, TEMPORARY]
  - availability: json
  - booking_rules: json

### ServiceOffering
Services provided by professional:
- Base Fields
  - professional: ForeignKey to MedicalProfessional
  - service_name: string
  - description: text
  - duration: integer (minutes)
  - cost: decimal
  - insurance_accepted: boolean

## Relationships
- MedicalProfessional -> User (OneToOne)
- MedicalProfessional -> Address (ManyToMany)
- MedicalProfessional -> ProfessionalSchedule (OneToMany)
- MedicalProfessional -> ServiceOffering (OneToMany)

## Indexing
- license_number: unique index
- provider_type + specialization: composite index
- location: spatial index
- verification_status: index
