# Appointment Models

## Note: Calendar Integration Strategy
Calendar integration implementation to be determined based on:
- External service requirements
- Synchronization needs
- Privacy and security standards
- Failover requirements

## Appointment
Core appointment management:
- Base Fields (Required)
  - identifier: unique identifier (UUID)
  - patient: foreign key to Patient
  - provider: foreign key to MedicalProfessional
  - datetime_start: datetime
  - datetime_end: datetime
  - status: enum[SCHEDULED, CONFIRMED, CANCELLED, COMPLETED]
  - type: enum[IN_PERSON, VIRTUAL, PHONE]
  
- Calendar Integration (Implementation Pending)
  NOTE: External calendar integration strategy to be determined
  Key considerations:
  - Provider calendar sync
  - Patient calendar sync
  - Multiple provider support
  - Conflict resolution
  - Failover handling

## TimeSlot
Availability management:
- Base Fields (Required)
  - provider: foreign key to MedicalProfessional
  - start_time: datetime
  - end_time: datetime
  - status: enum[AVAILABLE, BOOKED, BLOCKED]
  - recurrence_pattern: json (implementation details pending)

## SchedulingRules
Provider scheduling configuration:
- Base Fields (Required)
  - provider: foreign key to MedicalProfessional
  - availability_config: json (implementation details pending)
  - booking_rules: json (implementation details pending)

## Integration Options (To Be Evaluated)

### Calendar Services
Potential external calendar integrations:
- Google Calendar API
  - Real-time calendar sync
  - Free/busy lookups
  - Event management
  
- Microsoft Graph Calendar API
  - Office 365 integration
  - Teams meeting integration
  - Outlook calendar sync

- Apple Calendar API
  - iCloud calendar integration
  - iOS device sync
  - Local calendar sync

### Telehealth Platforms
Video consultation integrations:
- Zoom Healthcare API
  - HIPAA compliance
  - Waiting room support
  - Session management

- Twilio Video API
  - WebRTC integration
  - Recording capabilities
  - Multi-party sessions

### Practice Management Systems
EMR/EHR system integrations:
- Epic API
- Cerner API
- Athenahealth API

### Considerations for Selection
Final integration choices will depend on:
- HIPAA compliance requirements
- Cost and licensing
- API reliability and support
- Integration complexity
- User experience requirements
- Market adoption rates

## API Implementation (Pending)
Integration architecture to be determined based on:
- Selected service providers
- Security requirements
- Scalability needs
- Redundancy requirements
- Offline capabilities

## Relationships
- Appointment -> Patient (ManyToOne)
- Appointment -> MedicalProfessional (ManyToOne)
- TimeSlot -> MedicalProfessional (ManyToOne)
- SchedulingRules -> MedicalProfessional (OneToOne)

## Indexing
- datetime_start, datetime_end: composite index
- provider + status: composite index
- identifier: unique index
