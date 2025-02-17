from django.shortcuts import render

def home(request):
    """
    View for the home page
    """
    return render(request, 'home.html')
