from django.contrib import admin
from .models import Apartment, Garden, Land, Villa, Store
from .models import Apartment
from .forms import ApartmentAdminForm,LandAdminForm,GardenAdminForm,VillaAdminForm,StoreAdminForm
from accounts.custom_admin import custom_admin_site

class ApartmentAdmin(admin.ModelAdmin):
    form=ApartmentAdminForm
    list_display = ('title', 'build_year', 'rooms', 'floor')
    search_fields = ['title', 'location']

class GardenAdmin(admin.ModelAdmin):
    list_display = ('title', 'build_year', 'has_gazebo', 'has_pool')
    search_fields = ['title', 'location']

class LandAdmin(admin.ModelAdmin):
    list_display = ('title', 'area', 'price')
    search_fields = ['title', 'location']

class VillaAdmin(admin.ModelAdmin):
    list_display = ('title', 'build_year', 'yard_area', 'parkings')
    search_fields = ['title', 'location']

class StoreAdmin(admin.ModelAdmin):
    list_display = ('title', 'build_year', 'floor', 'parkings')
    search_fields = ['title', 'location']


custom_admin_site.register(Apartment,ApartmentAdmin)
custom_admin_site.register(Land,LandAdmin)
custom_admin_site.register(Store,StoreAdmin)
custom_admin_site.register(Villa,VillaAdmin)
custom_admin_site.register(Garden,GardenAdmin)