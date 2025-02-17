from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Message

@login_required
def inbox(request):
    """View for user's message inbox"""
    received_messages = Message.objects.filter(recipient=request.user).order_by('-created_at')
    unread_count = received_messages.filter(read=False).count()
    
    return render(request, 'messages/inbox.html', {
        'messages': received_messages,
        'unread_count': unread_count
    })

@login_required
def compose(request):
    """View for composing new messages"""
    if request.method == 'POST':
        recipient_id = request.POST.get('recipient')
        subject = request.POST.get('subject')
        content = request.POST.get('message')
        
        # Create new message
        message = Message.objects.create(
            sender=request.user,
            recipient_id=recipient_id,
            subject=subject,
            content=content
        )
        
        messages.success(request, 'Message sent successfully')
        return redirect('messages:inbox')
        
    return render(request, 'messages/compose.html')

@login_required
def message_detail(request, pk):
    """View for reading a specific message"""
    try:
        message = Message.objects.get(pk=pk, recipient=request.user)
        if not message.read:
            message.read = True
            message.save()
        return render(request, 'messages/detail.html', {'message': message})
    except Message.DoesNotExist:
        messages.error(request, 'Message not found')
        return redirect('messages:inbox')
