from django.urls import path
from . import views

app_name='contracts'
urlpatterns=[
    path('my/', views.my_contracts, name='my_contracts'),
     path('detail/<int:contract_id>/', views.contract_detail, name='contract_detail'),
     path('agent_contracts/', views.agent_contracts, name='agent_contracts'),
     path('contract_detail/<int:serial>/', views.contract_detail, name='contract_detail'),
]
