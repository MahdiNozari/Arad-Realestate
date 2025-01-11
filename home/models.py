from django.db import models
from django.conf import settings
from accounts.models import Customer
from django.urls import reverse
from django.utils.text import slugify

class File(models.Model):
    title = models.CharField(max_length=50)
    description = models.CharField(max_length=150, blank=True)
    area = models.PositiveIntegerField()
    price = models.BigIntegerField(blank=True, null=True)
    prepayment = models.BigIntegerField(blank=True, null=True)
    rent = models.BigIntegerField(blank=True, null=True)
    owner = models.ForeignKey(Customer, on_delete=models.CASCADE, related_name='properties')
    images = models.ImageField(blank=True, null=True)
    location = models.TextField()
    latitude = models.FloatField(blank=True,null=True)  
    longitude = models.FloatField(blank=True,null=True) 
    is_rent = models.BooleanField(default=False)
    is_sale = models.BooleanField(default=False)
    commercial = models.BooleanField(default=False)
    image_1 = models.ImageField(blank=True, null=True)  # تصویر دوم
    image_2 = models.ImageField(blank=True, null=True)  # تصویر سوم
    image_3 = models.ImageField(blank=True, null=True)  

    def __str__(self):
        return self.title
    


class Apartment(File):
    floor = models.PositiveIntegerField()
    parkings = models.PositiveIntegerField()
    rooms = models.PositiveIntegerField()
    build_year = models.PositiveIntegerField(default=0)
    basement = models.BooleanField(default=False)
    elevator = models.BooleanField(default=False)

    def __str__(self):
        return f"Apartment: {self.title}"
    
    def get_absolute_url(self):
        return reverse('home:apartment-detail', args=[self.title])


class Garden(File):
    build_year = models.PositiveIntegerField()
    has_gazebo = models.BooleanField(default=False)
    has_pool = models.BooleanField(default=False)
    yard_area = models.PositiveIntegerField()

    def __str__(self):
        return f"Garden: {self.title}"
    
    def get_absolute_url(self):
        return reverse('home:garden-detail', args=[self.title])

class Land(File):

    def __str__(self):
        return f"Land: {self.title}"

    def get_absolute_url(self):
        return reverse('home:land-detail', args=[self.title])

class Villa(File):
    build_year = models.PositiveIntegerField()
    yard_area = models.PositiveIntegerField()
    parkings = models.PositiveIntegerField()
    rooms = models.PositiveIntegerField(default=0)
    basement = models.BooleanField(default=False)
    def __str__(self):
        return f"Villa: {self.title}"
    
    def get_absolute_url(self):
        return reverse('home:villa-detail', args=[self.title])


class Store(File):
    build_year = models.PositiveIntegerField()
    floor = models.PositiveIntegerField(blank=True, null=True)
    parkings = models.PositiveIntegerField()

    def __str__(self):
        return f"Store: {self.title}"
    
    def get_absolute_url(self):
        return reverse('home:store-detail', args=[self.title])
