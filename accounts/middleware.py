from django.shortcuts import redirect
from django.contrib import messages
from .models import Agent,Customer

class AdminAccessMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        if request.path.startswith('/admin/') and request.user.is_authenticated and isinstance(request, Customer):
            messages.error(request, "You do not have permission to access the admin panel.")
            return redirect('home:home')  
        return self.get_response(request)
