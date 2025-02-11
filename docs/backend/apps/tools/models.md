# Tools App Models

NOTE: This is an initial implementation focusing on core functionality.
Additional tools and features will be added in future iterations.

## Common Fields
Fields shared across models:
- Audit Information (Auto-generated)
  - created_at: timestamp
  - updated_at: timestamp
  - created_by: foreign key to User
  - updated_by: foreign key to User

## HealthCalculator Model
Basic health calculation tools:
- Basic Information
  - name: string (required)
  - type: enum[BMI, CALORIE, HYDRATION] (required)
  - formula: json (required)
  - description: text (required)
  - status: enum[ACTIVE, DEPRECATED] (required)

## AssessmentTool Model
Simple health assessment questionnaires:
- Basic Information
  - title: string (required)
  - category: enum[MENTAL_HEALTH, PHYSICAL_FITNESS, NUTRITION] (required)
  - questions: json (required)
  - scoring_logic: json (required)
  - status: enum[DRAFT, ACTIVE, ARCHIVED] (required)

## Relationships
- HealthCalculator -> User (creator reference)
- AssessmentTool -> User (creator reference)

## Indexing
- HealthCalculator.type: index
- AssessmentTool.category + status: composite index

## Future Enhancements (Planned)
- Evidence-based reference system
- Advanced calculation engines
- Comprehensive assessment frameworks
- Integration with wearables and EHR
- Detailed reporting and analytics
- Tool categorization system
