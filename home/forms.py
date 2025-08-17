from django import forms
from .models import File,Apartment,Villa,Land,Store,Garden

class AddApartmentForm(forms.ModelForm):
    class Meta:
        model = Apartment
        fields = ['title', 'description', 'location','price','prepayment','rent','floor','images','is_sale','is_rent','commercial','parkings', 'rooms','build_year','basement','elevator','area']

class AddVillaForm(forms.ModelForm):
    class Meta:
        model = Villa
        fields = ['title', 'description', 'location','price','prepayment','rent','images','is_sale','is_rent','commercial','parkings', 'rooms','build_year','area','yard_area']

class AddStoreForm(forms.ModelForm):
    class Meta:
        model = Store
        fields = ['title', 'description', 'location','price','prepayment','rent','images','is_sale','is_rent','commercial','parkings','build_year','area','floor']

class AddGardenForm(forms.ModelForm):
    class Meta:
        model = Garden
        fields = ['title', 'description', 'location','price','prepayment','rent','images','is_sale','is_rent','commercial','has_gazebo','has_pool','build_year','area', 'yard_area']

class AddLandForm(forms.ModelForm):
    class Meta:
        model = Land
        fields = ['title', 'description', 'location','price','prepayment','rent','images','is_sale','is_rent','commercial','area']



class ApartmentAdminForm(forms.ModelForm):
    class Meta:
        model = Apartment
        fields = '__all__'

    class Media:
        css = {
            'all': ('https://cdnjs.cloudflare.com/ajax/libs/leaflet/1.9.3/leaflet.css',)
        }
        js = (
            'https://cdnjs.cloudflare.com/ajax/libs/leaflet/1.9.3/leaflet.js',
            '/static/js/admin_map.js',  
        )

class LandAdminForm(forms.ModelForm):
    class Meta:
        model = Land
        fields = '__all__'

    class Media:
        css = {
            'all': ('https://cdnjs.cloudflare.com/ajax/libs/leaflet/1.9.3/leaflet.css',)
        }
        js = (
            'https://cdnjs.cloudflare.com/ajax/libs/leaflet/1.9.3/leaflet.js',
            '/static/js/admin_map.js',  
        )

class VillaAdminForm(forms.ModelForm):
    class Meta:
        model = Villa
        fields = '__all__'

    class Media:
        css = {
            'all': ('https://cdnjs.cloudflare.com/ajax/libs/leaflet/1.9.3/leaflet.css',)
        }
        js = (
            'https://cdnjs.cloudflare.com/ajax/libs/leaflet/1.9.3/leaflet.js',
            '/static/js/admin_map.js',  
        )

class GardenAdminForm(forms.ModelForm):
    class Meta:
        model = Garden
        fields = '__all__'

    class Media:
        css = {
            'all': ('https://cdnjs.cloudflare.com/ajax/libs/leaflet/1.9.3/leaflet.css',)
        }
        js = (
            'https://cdnjs.cloudflare.com/ajax/libs/leaflet/1.9.3/leaflet.js',
            '/static/js/admin_map.js',  
        )

class StoreAdminForm(forms.ModelForm):
    class Meta:
        model = Store
        fields = '__all__'

    class Media:
        css = {
            'all': ('https://cdnjs.cloudflare.com/ajax/libs/leaflet/1.9.3/leaflet.css',)
        }
        js = (
            'https://cdnjs.cloudflare.com/ajax/libs/leaflet/1.9.3/leaflet.js',
            '/static/js/admin_map.js',  
        )


