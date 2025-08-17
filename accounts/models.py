from django.db import models
from django.contrib.auth.models import AbstractBaseUser,PermissionsMixin,Group,Permission
from .managers import UserManager
from django.conf import settings
from django.utils.timezone import now


class User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(unique=True)
    name = models.CharField(max_length=255)
    phone=models.CharField(max_length=11,default='',unique=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    date_joined = models.DateTimeField(auto_now_add=True)

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name','phone']

    class Meta:
        abstract = True


class Agent(User):
    ROLE_CHOICES = (
        ('junior', 'Junior Agent'),
        ('senior', 'Senior Agent'),
        ('manager', 'Manager'),
    )
    role = models.CharField(max_length=10, choices=ROLE_CHOICES, default='junior')

    
    groups = models.ManyToManyField(
        Group,
        related_name="agent_set",
        blank=True,
        help_text="The groups this agent belongs to.",
        verbose_name="groups",
    )
    user_permissions = models.ManyToManyField(
        Permission,
        related_name="agent_permissions",
        blank=True,
        help_text="Specific permissions for this agent.",
        verbose_name="user permissions",
    )

    def __str__(self):
        return f"{self.name} ({self.get_role_display()})"


class Customer(User):
    groups = models.ManyToManyField(
        Group,
        related_name="customer_set",
        blank=True,
        help_text="The groups this customer belongs to.",
        verbose_name="groups",
    )
    user_permissions = models.ManyToManyField(
        Permission,
        related_name="customer_permissions",
        blank=True,
        help_text="Specific permissions for this customer.",
        verbose_name="user permissions",
    )

    def __str__(self):
        return self.name
    
    
class OtpCode(models.Model):
    email = models.EmailField()
    code = models.PositiveSmallIntegerField()
    created = models.DateTimeField(auto_now=True)

    def __str__(self):
        return  f'{self.email} - {self.code} - {self.created}'