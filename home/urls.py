from django.urls import path
from . import views

app_name='home'
urlpatterns=[
    path('',views.HomeView.as_view(),name='home'),
    path('apartment-list/',views.ApartmentsView.as_view(),name='apartment-list'),
    path('land-list/',views.LandsView.as_view(),name='land-list'),
    path('villa-list/',views.VillaView.as_view(),name='villa-list'),
    path('store-list/',views.StoreView.as_view(),name='store-list'),
    path('garden-list/',views.GardenView.as_view(),name='garden-list'),
    path('apartment-list/<str:title>/', views.ApartmentDetailView.as_view(), name='apartment-detail'),
    path('land-list/<str:title>/', views.LandDetailView.as_view(), name='land-detail'),
    path('garden-list/<str:title>/', views.GardenDetailView.as_view(), name='garden-detail'),
    path('store-list/<str:title>/', views.StoreDetailView.as_view(), name='store-detail'),
    path('villa-list/<str:title>/', views.VillaDetailView.as_view(), name='villa-detail'),
    path('add-apartment/', views.AddApartment.as_view(), name='add-apartment'),
    path('add-villa/', views.AddVilla.as_view(), name='add-villa'),
    path('add-store/', views.AddStore.as_view(), name='add-store'),
    path('add-garden/', views.AddGarden.as_view(), name='add-garden'),
    path('add-land/', views.AddLand.as_view(), name='add-land'),
    path('properties/', views.property_list, name='property-list'),
    path('about/', views.AboutView.as_view(), name='about'),
    path('news1/',views.News1View.as_view(),name='news1'),
    path('news2/',views.News2View.as_view(),name='news2'),
    path('news3/',views.News3View.as_view(),name='news3'),
    path('news4/',views.News4View.as_view(),name='news4'),
    path('elahiye/',views.ElahiyeView.as_view(),name='elahiye'),
    path('west/',views.WestView.as_view(),name='west'),
    path('ekbatan/',views.Ekabataniew.as_view(),name='ekbatan'),
    path('tehranpars/',views.ParsView.as_view(),name='pars'),
    path('property-map/', views.property_map, name='property-map'),
]
