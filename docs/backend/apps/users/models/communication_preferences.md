# Communication Preferences Models

## CommunicationChannel
Supported communication methods:
- Base Fields
  - id: unique identifier (UUID)
  - channel_type: enum[EMAIL, SMS, PUSH, IN_APP, VOICE]
  - identifier: string (email address, phone number, device token)
  - is_verified: boolean
  - verification_date: datetime
  - is_active: boolean

## NotificationType
Different types of notifications:
- Base Fields
  - id: unique identifier (UUID)
  - code: string (unique identifier)
  - category: enum[SYSTEM, SECURITY, APPOINTMENT, MEDICAL, BILLING, MARKETING]
  - name: string
  - description: text
  - is_mandatory: boolean (some notifications can't be disabled)

## UserChannelPreference
Links users to their preferred channels:
- Base Fields
  - user: foreign key to User
  - channel: foreign key to CommunicationChannel
  - is_primary: boolean
  - do_not_disturb: json {
    enabled: boolean,
    start_time: time,
    end_time: time,
    timezone: string
  }
  - delivery_schedule: enum[IMMEDIATE, BATCHED, SCHEDULED]
  - scheduled_time: time (for scheduled delivery)

## NotificationPreference
User preferences for each notification type:
- Base Fields
  - user: foreign key to User
  - notification_type: foreign key to NotificationType
  - is_enabled: boolean (defaults to true for mandatory)
  - preferred_channel: foreign key to UserChannelPreference
  - frequency: enum[IMMEDIATELY, DAILY_DIGEST, WEEKLY_DIGEST]
  - quiet_hours: json {
    enabled: boolean,
    start_time: time,
    end_time: time,
    days: array[MONDAY-SUNDAY]
  }

## Relationships
- User -> CommunicationChannel (ManyToMany through UserChannelPreference)
- User -> NotificationType (ManyToMany through NotificationPreference)
- NotificationPreference -> UserChannelPreference (ManyToOne)

## Indexing
- channel_type + identifier: unique composite index
- user + notification_type: unique composite index
- user + channel: unique composite index
