# Account Models

## User
Extends Django's AbstractUser model:
- Base Fields (All Required)
  - username: unique identifier
  - email: verified email address
  - password: hashed password
  - first_name: user's first name
  - last_name: user's last name
  - date_joined: account creation date (auto-generated)
  - last_login: last login timestamp (auto-generated)
- Custom Fields
  - user_type: enum[PATIENT, DOCTOR, ADMIN, STAFF] (required)
  - status: enum[ACTIVE, INACTIVE, SUSPENDED, PENDING_VERIFICATION] (required)
  - email_verified: boolean (required, default: false)
  - phone_verified: boolean (required, default: false)
  - two_factor_enabled: boolean (optional)
  - account_locked: boolean (required, default: false)
  - login_attempts: integer (required, default: 0)
- Consent Information
  - consent_status: OneToOne to UserConsentStatus
  - consents: OneToMany to UserConsent
  - requires_consent_update: boolean (computed)

## Profile
Extended user information:
- Personal Information
  - date_of_birth: date (required for patients, optional for staff)
  - gender: enum[MALE, FEMALE, OTHER, PREFER_NOT_TO_SAY] (optional)
  - blood_type: enum[A+, A-, B+, B-, O+, O-, AB+, AB-] (optional)
  - profile_picture: image (optional)
  - bio: text (optional)
- Contact Information
  - phone_number: string (required)
  - addresses: ManyToMany to Address through AddressRelation
  - emergency_contacts: OneToMany to EmergencyContact
  - communication_channels: ManyToMany to CommunicationChannel through UserChannelPreference
  - notification_preferences: ManyToMany to NotificationType through NotificationPreference
- Preferences (All Optional)
  - language: string (default: 'en')
  - timezone: string (default: 'UTC')

## HealthcareProvider
Extended profile for medical professionals:
- Professional Information (All Required)
  - license_number: string
  - specializations: array
  - qualifications: array
  - years_of_experience: integer
  - practicing_since: date
- Verification (All Required)
  - license_verified: boolean
  - verification_documents: array
  - verification_status: enum[PENDING, VERIFIED, REJECTED]
- Practice Details
  - hospital_affiliations: array (required)
  - office_hours: json (required)
  - consultation_fee: decimal (required)
  - available_for_telemedicine: boolean (optional)

## AccountSecurity
Security-related information:
- Security Settings
  - password_last_changed: timestamp
  - security_questions: array
  - failed_login_attempts: integer
  - last_password_reset: timestamp
- Access Control (Token implementation pending)
  - NOTE: Token management strategy to be determined
  - Options under consideration:
    * Dedicated token model
    * External OAuth provider
    * Third-party authentication service
  - Final implementation will be based on:
    * Security requirements
    * Scalability needs
    * Compliance standards
- Activity Tracking
  - last_activity: timestamp
  - current_session_id: string
  - active_devices_count: integer
  - activity_logs: foreign key to ActivityLog (one-to-many)
  - audit_trails: foreign key to AuditTrail (one-to-many)

## Permissions
NOTE: Permission system structure to be determined.
Key considerations for implementation:
- Role-based access control requirements
- Integration with Django's authentication system
- Compliance with healthcare security standards
- Scalability needs
- Audit requirements

The final permission structure will be designed after:
- Security architecture review
- Regulatory compliance assessment
- System access pattern analysis
- Administrative workflow requirements

## Integration
External service connections:
- Third-party Authentications
  - oauth_providers: array
  - linked_accounts: json
  - social_connections: array
- API Access
  - api_keys: array
  - webhook_urls: array
  - integration_settings: json

## Relationships (All Required)
- User -> Profile (OneToOne)
- User -> HealthcareProvider (OneToOne, required only for doctors)
- User -> AccountSecurity (OneToOne)
- User -> Integration (OneToOne)
- User -> UserConsentStatus (OneToOne)
- User -> UserConsent (OneToMany)
- User -> CommunicationChannel (ManyToMany through UserChannelPreference)
- User -> NotificationType (ManyToMany through NotificationPreference)
- Note: Permission relationships will be defined once permission system is designed

## Indexing
- username: unique index
- email: unique index
- phone_number: unique index
- license_number: unique index (for healthcare providers)
