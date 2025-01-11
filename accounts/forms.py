from django import forms
from .models import Agent,Customer,OtpCode
from django.core.exceptions import ValidationError
from django.contrib.auth.forms import ReadOnlyPasswordHashField
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import Permission
from home.models import File
from django.contrib.auth.models import Permission,Group
from django.contrib.contenttypes.models import ContentType
from django.contrib.admin.widgets import FilteredSelectMultiple
from django.contrib.auth.hashers import make_password

class RegisterForm(forms.Form):
    fullname = forms.CharField(label='full name')
    password1 = forms.CharField(label='your password', widget=forms.PasswordInput)
    password2=forms.CharField(label='confirm password', widget=forms.PasswordInput)
    email = forms.EmailField(label='Your email')
    phone = forms.CharField(max_length=11, label='your phone number')

    def clean_email(self):
        email = self.cleaned_data['email']
        user = Customer.objects.filter(email=email).exists()
        if user:
            raise ValidationError('invalid email')
        OtpCode.objects.filter(email=email).delete()
        return email

    def clean_phone(self):
        phone = self.cleaned_data['phone']
        user = Customer.objects.filter(phone=phone).exists()
        if user:
            raise ValidationError('invalid phone number')
        return phone
    
    def clean_password2(self):
        cd = self.cleaned_data
        if cd['password1'] and cd['password2'] and cd['password1'] != cd['password2']:
            raise ValidationError('passwords dont match')
        return cd['password2']

class VerifyForm(forms.Form):
    code=forms.IntegerField()

class LoginForm(forms.Form):
    email = forms.EmailField(label='Your email')
    password = forms.CharField(label='Your Password', widget=forms.PasswordInput())



class CustomerCreationForm(UserCreationForm):
    """Form for creating a new Customer."""
    class Meta:
        model = Customer
        fields = ['email', 'phone', 'name', 'password1', 'password2']




class AddAgentForm(forms.ModelForm):
    """
    A form for creating new agents, similar to Django's default admin "Change Agent Form."
    """
    password1 = forms.CharField(
        widget=forms.PasswordInput,
        label="Password",
        required=True
    )
    password2 = forms.CharField(
        widget=forms.PasswordInput,
        label="Confirm Password",
        required=True
    )
    groups = forms.ModelMultipleChoiceField(
        queryset=Group.objects.all(),
        required=False,
        widget=FilteredSelectMultiple("Groups", is_stacked=False),
        label="Groups"
    )
    user_permissions = forms.ModelMultipleChoiceField(
        queryset=Permission.objects.all(),
        required=False,
        widget=FilteredSelectMultiple("User permissions", is_stacked=False),
        label="User Permissions"
    )

    class Meta:
        model = Agent
        fields = [
            'name', 
            'email',
            'phone', 
            'role', 
            'is_active', 
            'is_staff', 
            'is_superuser', 
            'groups', 
            'user_permissions'
        ]

    def clean_password2(self):
        """
        Validates that the two password entries match.
        """
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("The two password fields didn't match.")
        return password2

    def save(self, commit=True):
        """
        Save the agent, set the password, and handle groups and permissions.
        """
        agent = super().save(commit=False)
        agent.set_password(self.cleaned_data['password1'])
        if commit:
            agent.save()
            self.save_m2m()
        return agent
    
class ChangeAgentForm(forms.ModelForm):
    """
    A form for updating existing agents with an optional password reset field.
    """
    groups = forms.ModelMultipleChoiceField(
        queryset=Group.objects.all(),
        required=False,
        widget=FilteredSelectMultiple("Groups", is_stacked=False),
        label="Groups"
    )
    user_permissions = forms.ModelMultipleChoiceField(
        queryset=Permission.objects.all(),
        required=False,
        widget=FilteredSelectMultiple("User permissions", is_stacked=False),
        label="User Permissions"
    )
    new_password = forms.CharField(
        required=False,
        widget=forms.PasswordInput(attrs={'autocomplete': 'new-password'}),
        label="Reset Password",
        help_text="Leave blank if you don't want to change the password."
    )

    class Meta:
        model = Agent
        fields = [
            'name',
            'email',
            'phone',
            'role',
            'is_active',
            'is_staff',
            'is_superuser',
            'groups',
            'user_permissions',
        ]

    def save(self, commit=True):
        """
        Save the updated agent and handle password reset, groups, and permissions.
        """
        agent = super().save(commit=False)

        
        new_password = self.cleaned_data.get('new_password')
        if new_password:
            agent.password = make_password(new_password)

        if commit:
            agent.save()
            self.save_m2m()

        return agent