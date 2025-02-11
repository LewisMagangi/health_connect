# Audit Logging Models

## ActivityLog
Comprehensive logging system for all user-related activities:
- Base Fields
  - log_id: unique identifier (UUID)
  - timestamp: datetime with timezone
  - user_id: foreign key to User
  - event_type: enum[LOGIN, LOGOUT, PASSWORD_CHANGE, etc.]
  - status: enum[SUCCESS, FAILURE, ATTEMPT]
  - ip_address: string
  - location_data: json (geolocation info)
  
- Device Information
  - device_id: string
  - device_type: string
  - browser: string
  - operating_system: string
  - user_agent: string

- Event Details
  - description: text
  - metadata: json
  - related_objects: json
  - severity_level: enum[INFO, WARNING, ERROR]

- Security Context
  - session_id: string
  - authentication_method: string
  - access_type: string

## AuditTrail
System-wide audit logging for compliance and security:
- Base Fields
  - audit_id: unique identifier (UUID)
  - timestamp: datetime with timezone
  - actor_id: foreign key to User
  - action: enum[CREATE, READ, UPDATE, DELETE]
  - resource_type: string
  - resource_id: string

- Change Details
  - previous_state: json
  - new_state: json
  - changes_summary: text
  - justification: text (optional)

- Compliance
  - retention_period: integer
  - compliance_tags: array
  - data_sensitivity: enum[PUBLIC, INTERNAL, CONFIDENTIAL, RESTRICTED]
  - regulatory_categories: array[HIPAA, GDPR, etc.]
