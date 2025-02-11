# Address Models

## Address
Base model for all address types:
- Base Fields
  - id: unique identifier (UUID)
  - address_type: enum[HOME, WORK, PRACTICE, OTHER]
  - street_line1: string (required)
  - street_line2: string (optional)
  - city: string (required)
  - state: string (required)
  - country: string (required)
  - postal_code: string (required)
  - is_primary: boolean (default: false)
  - is_verified: boolean (default: false)
  - coordinates: Point (optional, for geolocation)

## EmergencyContact
Emergency contact information:
- Base Fields
  - id: unique identifier (UUID)
  - user: foreign key to User (required)
  - full_name: string (required)
  - relationship: string (required)
  - primary_phone: string (required)
  - secondary_phone: string (optional)
  - email: string (optional)
  - is_primary: boolean (default: false)
  - notify_on_emergency: boolean (default: true)
- Address
  - foreign key to Address model (optional)
  - can reuse existing addresses

## AddressRelation
Links addresses to users/providers:
- Fields
  - address: foreign key to Address
  - content_type: ContentType (User, HealthcareProvider, etc.)
  - object_id: ID of related object
  - relationship_type: enum[RESIDENTIAL, PRACTICE, BILLING, EMERGENCY]

## Relationships
- User -> Address (ManyToMany through AddressRelation)
- HealthcareProvider -> Address (ManyToMany through AddressRelation)
- EmergencyContact -> Address (ForeignKey)

## Indexing
- postal_code: index
- city: index
- country: index
- coordinates: spatial index
