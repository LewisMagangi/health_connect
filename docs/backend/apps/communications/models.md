# Unified Communications Model

## Communication Session
Base structure for all communication types:
- sessionId: unique identifier
- participants: array of users
- type: enum[MESSAGE, VIDEO, VOICE]
- status: enum[ACTIVE, ENDED]
- startTime: timestamp
- endTime: timestamp
- metadata: session-specific data

## Message Communication
Extends Communication Session:
- messageContent: text/attachments
- readStatus: per participant
- messageType: enum[TEXT, FILE, IMAGE]

## Video Communication
Extends Communication Session:
- streamIds: per participant
- quality: connection quality metrics
- recording: optional recording settings

## Voice Communication
Extends Communication Session:
- audioChannels: per participant
- quality: connection metrics
- recording: optional recording settings

## Integration Points
- Unified notifications system
- Common authentication
- Shared file storage
- Cross-communication features (switch between types)
