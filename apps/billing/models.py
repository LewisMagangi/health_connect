from django.db import models
from django.conf import settings

class Invoice(models.Model):
    PENDING = 'PENDING'
    PAID = 'PAID'
    OVERDUE = 'OVERDUE'
    CANCELLED = 'CANCELLED'

    STATUS_CHOICES = [
        (PENDING, 'Pending'),
        (PAID, 'Paid'),
        (OVERDUE, 'Overdue'),
        (CANCELLED, 'Cancelled'),
    ]

    patient = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='invoices')
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField()
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default=PENDING)
    due_date = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f"Invoice {self.id} - {self.patient.username} - {self.status}"

class Payment(models.Model):
    PAYMENT_METHODS = (
        ('CREDIT_CARD', 'Credit Card'),
        ('DEBIT_CARD', 'Debit Card'),
        ('BANK_TRANSFER', 'Bank Transfer'),
        ('CASH', 'Cash'),
        ('INSURANCE', 'Insurance'),
    )

    invoice = models.ForeignKey(Invoice, on_delete=models.CASCADE, related_name='payments')
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    payment_method = models.CharField(max_length=20, choices=PAYMENT_METHODS)
    transaction_id = models.CharField(max_length=100, unique=True)
    payment_date = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=20)
    notes = models.TextField(blank=True)

    def __str__(self):
        return f"Payment {self.transaction_id} for Invoice #{self.invoice.id}"
