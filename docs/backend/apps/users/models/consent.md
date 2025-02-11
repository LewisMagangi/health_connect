# User Consent Models

## UserConsent
Tracks individual consent events:
- Base Fields
  - id: unique identifier (UUID)
  - user: foreign key to User (required)
  - consent_type: enum[TERMS_OF_SERVICE, PRIVACY_POLICY, DATA_SHARING, MEDICAL_DATA_ACCESS]
  - version: string (required) - version of the policy/terms accepted
  - timestamp: datetime (required, auto-generated)
  - ip_address: string (required)
  - user_agent: string (required)

## ConsentVersion
Manages versions of different consent documents:
- Base Fields
  - id: unique identifier (UUID)
  - consent_type: enum[TERMS_OF_SERVICE, PRIVACY_POLICY, DATA_SHARING, MEDICAL_DATA_ACCESS]
  - version: string (required)
  - effective_date: datetime (required)
  - content: text (required) - actual content of the terms/policy
  - summary_of_changes: text (optional) - key changes from previous version
  - is_active: boolean (default: true)

## UserConsentStatus
Current consent status for quick reference:
- Base Fields
  - user: foreign key to User (required)
  - latest_terms_version: string
  - terms_accepted_at: datetime
  - latest_privacy_version: string
  - privacy_accepted_at: datetime
  - latest_data_sharing_version: string
  - data_sharing_accepted_at: datetime
  - all_required_consents_provided: boolean

## Relationships
- User -> UserConsent (OneToMany)
- User -> UserConsentStatus (OneToOne)
- UserConsent -> ConsentVersion (ManyToOne)

## Indexing
- user + consent_type: composite index
- timestamp: index
- version: index
