from django.db import models
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.conf import settings
from django.utils.timezone import now
from accounts.models import Customer,Agent


class VisitRequestCart(models.Model):
    user = models.OneToOneField(Customer, on_delete=models.CASCADE, related_name="visit_cart") 
    @property
    def total_cost(self):
        # محاسبه هزینه فقط برای درخواست‌های پرداخت‌نشده
        return self.requests.filter(is_paid=False).count() * 100   


class VisitRequest(models.Model):
    STATUS_CHOICES = [
        ('pending', 'در انتظار پرداخت'),
        ('in_progress', 'در حال انجام'),
        ('completed', 'انجام شده'),
    ]
    cart = models.ForeignKey(VisitRequestCart, on_delete=models.CASCADE, related_name="requests")
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    file = GenericForeignKey('content_type', 'object_id')
    created_at = models.DateTimeField(default=now)
    is_paid = models.BooleanField(default=False)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending')  # فیلد وضعیت
    done = models.BooleanField(default=False)
    request_assigned = models.ForeignKey(Agent, null=True, blank=True, on_delete=models.SET_NULL, related_name="assigned_requests")
    def __str__(self):
        return f"درخواست بازدید برای {self.file} توسط {self.cart.user.name}"
    


class ExpertiseRequest(models.Model):
    STATUS_CHOICES = [
        ('pending', 'در انتظار پرداخت'),
        ('in_progress', 'در حال انجام'),
        ('completed', 'تکمیل شده'),
    ]

    user = models.ForeignKey(Customer, on_delete=models.CASCADE, related_name="expertise_requests")
    property_title = models.CharField(max_length=255)
    property_type = models.CharField(max_length=50, choices=[
        ('villa', 'ویلا'),
        ('apartment', 'آپارتمان'),
        ('land', 'زمین'),
        ('store', 'فروشگاه'),
        ('garden', 'باغ')
    ])
    description = models.TextField(blank=True, null=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending')
    created_at = models.DateTimeField(default=now)
    expert_assigned = models.ForeignKey(Agent, null=True, blank=True, on_delete=models.SET_NULL, related_name="assigned_expertises")
    expertise_fee = models.DecimalField(max_digits=10, decimal_places=2, default=500)
    is_paid = models.BooleanField(default=False)

    def __str__(self):
        return f"درخواست کارشناسی برای {self.property_title} توسط {self.user.name}"

    class Meta:
        verbose_name = 'درخواست کارشناسی'
        verbose_name_plural = 'درخواست‌های کارشناسی'

    

