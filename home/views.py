from django.shortcuts import render,get_object_or_404,redirect
from django.views.generic import ListView
from django.views import View
from .forms import  AddApartmentForm,AddVillaForm,AddStoreForm,AddGardenForm,AddLandForm
from .models import Apartment,Land,Villa,Store,Garden
from django.contrib import messages
from accounts.models import Customer
from django.contrib.auth.mixins import LoginRequiredMixin
import json

class HomeView(View):
    def get(self,request):
        return render(request, 'home/home.html')

class ApartmentsView(ListView):
    model=Apartment
    template_name='home/apartments.html'
    context_object_name='apartments'

class LandsView(ListView):
    model=Land
    template_name='home/lands.html'
    context_object_name='lands'

class VillaView(ListView):
    model=Villa
    template_name='home/villa.html'
    context_object_name='villas'

class StoreView(ListView):
    model=Store
    template_name='home/store.html'
    context_object_name='stores'

class GardenView(ListView):
    model=Garden
    template_name='home/garden.html'
    context_object_name='gardens'

class ApartmentDetailView(View):
    def get(self, request, title):
        details = get_object_or_404(Apartment, title=title)
        return render(request, 'home/apartment-detail.html', {'details': details})
    
class LandDetailView(View):
    def get(self, request, title):
        details = get_object_or_404(Land, title=title)
        return render(request, 'home/land-detail.html', {'details': details})

class GardenDetailView(View):
    def get(self, request, title):
        details = get_object_or_404(Garden, title=title)
        return render(request, 'home/garden-detail.html', {'details': details})
    
class StoreDetailView(View):
    def get(self, request, title):
        details = get_object_or_404(Store, title=title)
        return render(request, 'home/store-detail.html', {'details': details})
    
class VillaDetailView(View):
    def get(self, request, title):
        details = get_object_or_404(Villa, title=title)
        return render(request, 'home/villa-detail.html', {'details': details})
    
class AddApartment(LoginRequiredMixin, View):
    form_class=AddApartmentForm
    def get(self,request,*args,**kwargs):
        form=self.form_class
        return render(request,'home/add_apartment.html',{'form':form})
    def post(self,request,*args,**kwargs):
        form=self.form_class(request.POST, request.FILES)
        if form.is_valid():
            new_ad=form.save(commit=False)
            new_ad.latitude = request.POST.get('latitude')
            new_ad.longitude = request.POST.get('longitude')
            if isinstance(request.user,Customer):
                new_ad.owner = request.user
            else:
                messages.error(request,'you must login first','danger')
                return redirect('accounts:login')
            new_ad.save()
            print(request.FILES)
            return redirect('home:apartment-list')
        messages.error(request,'failed','danger')
        return redirect('home:add-apartment')

class AddVilla(View):
    form_class=AddVillaForm
    def get(self,request,*args,**kwargs):
        form=self.form_class
        return render(request,'home/add-villa.html',{'form':form})
    def post(self,request,*args,**kwargs):
        form=self.form_class(request.POST, request.FILES)
        if form.is_valid():
            new_ad=form.save(commit=False)
            new_ad.latitude = request.POST.get('latitude')
            new_ad.longitude = request.POST.get('longitude')
            if isinstance(request.user,Customer):
                new_ad.owner = request.user
            else:
                messages.error(request,'you must login first','danger')
                return redirect('accounts:login')
            new_ad.save()
            print(request.FILES)
            return redirect('home:villa-list')
        messages.error(request,'failed','danger')
        return redirect('home:add-villa')
    
class AddStore(View):
    form_class=AddStoreForm
    def get(self,request,*args,**kwargs):
        form=self.form_class
        return render(request,'home/add-store.html',{'form':form})
    def post(self,request,*args,**kwargs):
        form=self.form_class(request.POST, request.FILES)
        if form.is_valid():
            new_ad=form.save(commit=False)
            new_ad.latitude = request.POST.get('latitude')
            new_ad.longitude = request.POST.get('longitude')
            if isinstance(request.user,Customer):
                new_ad.owner = request.user
            else:
                messages.error(request,'you must login first','danger')
                return redirect('accounts:login')
            new_ad.save()
            print(request.FILES)
            return redirect('home:store-list')
        messages.error(request,'failed','danger')
        return redirect('home:add-store')
    
class AddGarden(View):
    form_class=AddGardenForm
    def get(self,request,*args,**kwargs):
        form=self.form_class
        return render(request,'home/add-garden.html',{'form':form})
    def post(self,request,*args,**kwargs):
        form=self.form_class(request.POST, request.FILES)
        if form.is_valid():
            new_ad=form.save(commit=False)
            new_ad.latitude = request.POST.get('latitude')
            new_ad.longitude = request.POST.get('longitude')
            if isinstance(request.user,Customer):
                new_ad.owner = request.user
            else:
                messages.error(request,'you must login first','danger')
                return redirect('accounts:login')
            new_ad.save()
            print(request.FILES)
            return redirect('home:garden-list')
        messages.error(request,'failed','danger')
        return redirect('home:add-garden')
    
class AddLand(View):
    form_class = AddLandForm

    def get(self, request, *args, **kwargs):
        form = self.form_class()
        return render(request, 'home/add-land.html', {'form': form})

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST, request.FILES)
        if form.is_valid():
            new_land = form.save(commit=False)
            new_land.latitude = request.POST.get('latitude')
            new_land.longitude = request.POST.get('longitude')

            # Ensure the user is logged in and is a Customer
            if request.user.is_authenticated:
                if isinstance(request.user, Customer):  # Change to match your Customer model
                    new_land.owner = request.user
                else:
                    messages.error(request, 'You must be a valid customer to add land.', 'danger')
                    return redirect('accounts:login')
            else:
                messages.error(request, 'You must be logged in to add land.', 'danger')
                return redirect('accounts:login')

            new_land.save()
            messages.success(request, 'Land added successfully!', 'success')
            return redirect('home:land-list')

        # If the form is not valid, show an error message
        messages.error(request, 'Form submission failed. Please check your inputs.', 'danger')
        return redirect('home:add-land')
    

from django.db.models import Q
def property_list(request):
    # دریافت فیلترها از URL
    max_price = request.GET.get('price')
    max_year = request.GET.get('year')
    min_area = request.GET.get('area')
    is_rent = request.GET.get('is_rent')
    is_sale = request.GET.get('is_sale')
    max_rent = request.GET.get('rent')
    max_prepayment=request.GET.get('prepayment')
    property_type = request.GET.get('property_type')

    # نتایج فیلتر شده برای هر مدل
    properties = []

    if property_type == 'apartment':
        properties = Apartment.objects.all()
    elif property_type == 'villa':
        properties = Villa.objects.all()
    elif property_type == 'store':
        properties = Store.objects.all()
    elif property_type == 'garden':
        properties = Garden.objects.all()
    elif property_type == 'land':
        properties = Land.objects.all()
    else:
        properties = list(Apartment.objects.all())
        properties.extend(Villa.objects.all())
        properties.extend(Store.objects.all())
        properties.extend(Garden.objects.all())
        properties.extend(Land.objects.all())

    # اعمال فیلترها
    if max_price:
        properties = [p for p in properties if p.price and p.price <= int(max_price)]
    if max_rent:
        properties = [p for p in properties if p.rent and p.rent <= int(max_rent)]
    if max_prepayment:
        properties = [p for p in properties if p.prepayment and p.prepayment <= int(max_prepayment)]
    if max_year:
        properties = [p for p in properties if p.build_year and p.build_year >= int(max_year)]
    if min_area:
        properties = [p for p in properties if p.area and p.area >= int(min_area)]
    if is_rent:
        properties = [p for p in properties if p.is_rent == (is_rent == 'true')]
    if is_sale:
        properties = [p for p in properties if p.is_sale == (is_sale == 'true')]

    # ارسال نتایج به تمپلیت
    return render(request, 'home/property_list.html', {'properties': properties})

class AboutView(View):
    def get(self, request):
        return render(request,'home/about.html')
    
class News1View(View):
    def get(self, request):
        return render(request,'home/news1.html')
    
class News2View(View):
    def get(self, request):
        return render(request,'home/news2.html')
    
class News3View(View):
    def get(self, request):
        return render(request,'home/news3.html')
    
class News4View(View):
    def get(self, request):
        return render(request,'home/news4.html')
    
class ElahiyeView(View):
    def get(self, request):
        return render(request,'home/elahiye.html')
    
class WestView(View):
    def get(self, request):
        return render(request,'home/west.html')
class Ekabataniew(View):
    def get(self, request):
        return render(request,'home/ekbatan.html')
    
class ParsView(View):
    def get(self, request):
        return render(request,'home/pars.html')
    
# views.py
import json
from django.shortcuts import render
from .models import Apartment, Garden, Land, Villa, Store

def property_map(request):
    apartments = Apartment.objects.all()
    gardens = Garden.objects.all()
    lands = Land.objects.all()
    villas = Villa.objects.all()
    stores = Store.objects.all()

    all_files = list(apartments) + list(gardens) + list(lands) + list(villas) + list(stores)

    file_data = [
        {
            "title": file.title,
            "description": file.description,
            "area": file.area,
            "images": file.images.url if file.images else None,
            "image1": file.image_1.url if file.image_1 else None,
            "image2": file.image_2.url if file.image_2 else None,
            "image3": file.image_3.url if file.image_3 else None,
            "is_sale": file.is_sale,
            "is_rent": file.is_rent,
            "commercial": file.commercial,
            "latitude": file.latitude,
            "longitude": file.longitude,
            "price": file.price,
            "rent": file.rent,
            "prepayment": file.prepayment,
            "type": file.__class__.__name__,
            "url": file.get_absolute_url()
        }
        for file in all_files
    ]

    return render(request, 'home/property_map.html', {'file_data': json.dumps(file_data)})
