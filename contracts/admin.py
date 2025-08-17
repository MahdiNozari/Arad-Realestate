from django.contrib import admin
from .models import Contract
from accounts.custom_admin import custom_admin_site
custom_admin_site.register(Contract)
# Register your models here.
