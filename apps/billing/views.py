from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Invoice

@login_required
def invoice_list(request):
    if request.user.is_staff:
        invoices = Invoice.objects.all()
    else:
        invoices = Invoice.objects.filter(patient=request.user)
    return render(request, 'billing/invoice_list.html', {'invoices': invoices})

@login_required
def invoice_detail(request, invoice_id):
    invoice = get_object_or_404(Invoice, id=invoice_id)
    if not request.user.is_staff and invoice.patient != request.user:
        messages.error(request, "You don't have permission to view this invoice.")
        return redirect('billing:invoice_list')
    return render(request, 'billing/invoice_detail.html', {'invoice': invoice})
