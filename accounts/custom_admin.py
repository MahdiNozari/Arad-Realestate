from django.contrib.admin import AdminSite
from django.contrib.auth.models import User
from django.contrib import admin
from django.contrib import messages
from django.shortcuts import redirect
from .models import Agent, Customer  # Adjust imports for your models

class CustomAdminSite(AdminSite):
    site_header = "Custom Admin Panel"
    site_title = "Custom Admin"
    index_title = "Welcome to the Custom Admin"

    def login(self, request, extra_context=None):
        if request.user.is_authenticated:
            # Allow superuser or staff members (and optionally Agents)
            if not (request.user.is_superuser or request.user.is_staff):
                messages.error(request, "You do not have permission to access the admin panel.")
                return redirect('home:home')
        return super().login(request, extra_context)
    
custom_admin_site = CustomAdminSite(name='custom_admin')

