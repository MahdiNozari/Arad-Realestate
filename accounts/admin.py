from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Customer, Agent,OtpCode
from .forms import CustomerCreationForm,AddAgentForm,ChangeAgentForm
from django.contrib.auth.models import Permission
from django.contrib.contenttypes.models import ContentType
from home.models import File
from .custom_admin  import custom_admin_site

class CustomerAdmin(UserAdmin):
    add_form = CustomerCreationForm
    model = Customer
    list_display = ['email', 'name', 'phone', 'is_active', 'date_joined']
    readonly_fields = ['date_joined']
    ordering = ['email']  
    fieldsets = (
        (None, {
            'fields': ('email', 'name', 'phone', 'password', 'is_active', 'date_joined'),
        }),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'name', 'phone', 'password1', 'password2'),
        }),
    )


class AgentAdmin(admin.ModelAdmin):
    add_form = AddAgentForm
    form = ChangeAgentForm
    list_display = ('name', 'email', 'phone', 'role', 'is_staff', 'is_active')
    list_filter = ('role', 'is_staff', 'is_active')


    fieldsets = (
        (None, {
            'fields': ('name', 'email', 'phone', 'role', 'is_active', 'is_staff', 'is_superuser')
        }),
        ('Permissions', {
            'fields': ('groups', 'user_permissions')
        }),
        ('Password Reset', {
            'fields': ('new_password',),
            'description': 'Reset the password for the agent (leave blank to retain the current password).',
        }),
    )


    add_fieldsets = (
        (None, {
            'fields': ('name', 'email', 'phone', 'password1', 'password2', 'role', 'is_active', 'is_staff', 'is_superuser')
        }),
        ('Permissions', {
            'fields': ('groups', 'user_permissions')
        }),
    )

    def get_fieldsets(self, request, obj=None):
        """
        Return fieldsets for add or change views.
        """
        if obj:  
            return self.fieldsets
        return self.add_fieldsets

    def get_form(self, request, obj=None, **kwargs):
        """
        Use AddAgentForm for adding and ChangeAgentForm for updating.
        """
        if obj is None:
            kwargs['form'] = self.add_form
        else:
            kwargs['form'] = self.form
        return super().get_form(request, obj, **kwargs)

    search_fields = ('name', 'email')
    ordering = ('name',)
    filter_horizontal = ('groups', 'user_permissions')
 

custom_admin_site.register(Agent,AgentAdmin)  
custom_admin_site.register(Customer,CustomerAdmin)    
custom_admin_site.register(OtpCode)
