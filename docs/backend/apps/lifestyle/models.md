# Lifestyle App Models

## Common Fields
Fields shared across models:
- Audit Information (Auto-generated)
  - created_at: timestamp
  - updated_at: timestamp
  - created_by: foreign key to User
  - updated_by: foreign key to User

## WellnessPlan Model
Tracks patient wellness goals and progress using evidence-based approaches:

- Plan Information
  - patient: foreign key to Patient (required)
  - title: string (required)
  - start_date: date (required)
  - end_date: date (required)
  - status: enum[ACTIVE, COMPLETED, PAUSED, UNDER_REVIEW]

- Goals Structure (stored as structured JSON)
  - domains: array of wellness domains
    * nutrition:
      - baseline_metrics:
        * daily_calories: number
        * macro_distribution: object
        * plant_based_meals: percentage
      - targets:
        * dietary_pattern: string
        * meal_frequency: number
        * hydration_goals: object
      - restrictions:
        * allergies: array
        * avoided_foods: array
      - interventions:
        * meal_planning: object
        * supplementation: array
    
    * exercise:
      - baseline_fitness:
        * cardio_capacity: object
        * strength_metrics: object
      - targets:
        * weekly_sessions: number
        * intensity_distribution: object
        * specific_activities: array
      - constraints:
        * physical_limitations: array
        * time_restrictions: object
      - progression_plan: object
    
    * sleep:
      - baseline_patterns:
        * average_duration: number
        * quality_metrics: object
      - targets:
        * bedtime_window: object
        * wake_window: object
        * total_hours: number
      - hygiene_practices:
        * evening_routine: array
        * morning_routine: array
      - environment_optimization: object
    
    * circadian_rhythm:
      - light_exposure:
        * morning_sunlight: object
        * daily_bright_light: object
        * evening_dimming: object
      - meal_timing:
        * eating_window: object
        * major_meals: array
      - temperature_regulation:
        * evening_cooling: object
        * sleep_temperature: number
      - activity_alignment:
        * exercise_timing: object
        * rest_periods: array
    
    * stress_management:
      - baseline_assessment:
        * stress_scores: object
        * key_stressors: array
      - targets:
        * daily_practices: array
        * weekly_activities: array
      - techniques:
        * breathing_exercises: array
        * meditation_goals: object
      - support_resources: array
    
    * habit_formation:
      - target_habits:
        * morning_routine: array
        * daily_practices: array
        * evening_routine: array
      - implementation:
        * triggers: array
        * tracking_method: string
        * reward_system: object
      - progression:
        * milestones: array
        * adaptation_points: array

  - tracking_configuration:
    * measurement_frequency: object per domain
    * data_sources: array of input methods
    * validation_rules: object
    * alert_thresholds: object
    
  - progress_metrics:
    * baseline_date: timestamp
    * review_frequency: string
    * milestone_definitions: array
    * success_criteria: object per domain

- Progress Tracking
  - review_schedule: json (required)
  - last_review_date: timestamp
  - progress_metrics: json
  - adherence_rate: decimal
  - patient_feedback: text
  - clinician_notes: text

- Adaptability
  - modifications_history: json
  - next_review_date: date
  - intervention_triggers: json (thresholds for alerts)

## HealthMetrics Model
Comprehensive health measurements and activities tracking:

- Basic Information
  - patient: foreign key to Patient (required)
  - timestamp: datetime (required)
  - source: enum[MANUAL_ENTRY, WEARABLE, PROVIDER_INPUT]

- Metric Types (enum)
  - ANTHROPOMETRIC: weight, height, BMI, body composition
  - CARDIOVASCULAR: blood pressure, heart rate, HRV
  - ACTIVITY: steps, exercise minutes, intensity
  - SLEEP: duration, quality, phases
  - NUTRITION: meals, water intake, supplements
  - BIOMETRICS: blood glucose, oxygen saturation
  - SUBJECTIVE: mood, energy, stress levels

- Data Storage
  - metric_type: string (choice from Metric Types)
  - value: json (standardized format per type)
  - metadata: json (source-specific details)
  - quality_score: decimal (data reliability indicator)

- Analysis Support
  - trend_indicators: json
  - correlation_flags: json
  - alert_thresholds: json

## Integration Points
- Wearable Devices
  - supported_devices: documented in integration specs
  - data_mapping: standardized format definitions
- External Systems
  - EHR integration capabilities
  - telehealth platform connections
  - analytics system feeds

## Relationships
- WellnessPlan -> Patient (ForeignKey)
- HealthMetrics -> Patient (ForeignKey)
- WellnessPlan -> HealthMetrics (implicit through Patient)

## Indexing
- WellnessPlan.patient + status: composite index
- HealthMetrics.patient + timestamp: composite index
- HealthMetrics.metric_type + timestamp: index
