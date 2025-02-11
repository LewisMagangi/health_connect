# Billing Models

## Note: Implementation Strategy
Final implementation details will be determined based on:
- Payment gateway requirements
- Accounting system integration needs
- Compliance standards
- Security requirements

## Invoice
Core billing record:
- Base Fields (Required)
  - identifier: unique identifier (UUID)
  - patient: foreign key to Patient
  - provider: foreign key to MedicalProfessional
  - issue_date: datetime
  - due_date: datetime
  - status: enum[DRAFT, ISSUED, PAID, OVERDUE, CANCELLED]

- Financial Details (Required)
  - currency: string
  - line_items: json (implementation pending)
  - subtotal: decimal
  - tax: decimal
  - discounts: json (implementation pending)
  - total: decimal

- Billing Cycle (Optional)
  - is_recurring: boolean
  - cycle_config: json (implementation pending)
  - next_generation: datetime

## Payment
Payment transaction records:
- Base Fields (Required)
  - identifier: unique identifier (UUID)
  - invoice: foreign key to Invoice
  - amount: decimal
  - timestamp: datetime
  - status: enum[PENDING, COMPLETED, FAILED, REFUNDED]

- Payment Details
  - method_type: enum[CARD, ACH, EXTERNAL]
  - provider_reference: string
  - metadata: json (implementation pending)

## Integration Options (To Be Evaluated)

### Payment Gateways
Potential integrations:
- Stripe API
- PayPal API
- Square API

### Accounting Systems
External system integrations:
- QuickBooks API
- Xero API
- FreshBooks API

### Banking Systems
Direct banking integrations:
- ACH processing
- Wire transfers
- Bank verification

## Security & Compliance
Implementation will follow:
- PCI-DSS requirements
- HIPAA guidelines
- Data protection standards
- Audit requirements

## Relationships
- Invoice -> Patient (ManyToOne)
- Invoice -> MedicalProfessional (ManyToOne)
- Payment -> Invoice (ManyToOne)

## Indexing
- identifier: unique index
- status: index
- due_date: index
- patient + status: composite index
