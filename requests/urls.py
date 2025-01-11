from django.urls import path
from . import views

app_name='requests'
urlpatterns = [
     path('add-to-visit-cart/<str:model_name>/<str:property_title>/', views.add_to_visit_cart, name='add_to_visit_cart'),
     path('request-expertise/', views.RequestExpertiseView.as_view(), name='request_expertise'),
     path('expertise-requests/', views.user_expertise_requests, name='user_expertise_requests'),
     path('expertise-request/pay/<int:pk>/', views.PayExpertiseRequestView.as_view(), name='pay_expertise_request'),
     path('remove-visit-request/<int:request_id>/', views.remove_visit_request, name='remove_visit_request'),
     path('all-requests/', views.all_requests, name='all_requests'),
     path('process-payment/<int:request_id>/', views.process_payment, name='process_payment'),
     path('remove-expertise-request/<int:pk>/', views.remove_expertise_request, name='remove_expertise_request'),
     path('manage_requests/', views.manage_expertise_requests, name='manage_expertise_requests'),
     path('agent_requests/', views.agent_expertise_requests, name='agent_expertise_requests'),
      path('request_details/<int:request_id>/', views.expertise_request_details, name='expertise_request_details'),
      path('expertise_request/cancel/<int:expertise_request_id>/', views.cancel_expertise_request, name='cancel_expertise_request'),
      path('available_requests/', views.available_visit_requests, name='available_visit_requests'),
      path('assign_request/<int:visit_request_id>/', views.assign_visit_request, name='assign_visit_request'),
      path('delete_request/<int:visit_request_id>/', views.delete_visit_request, name='delete_visit_request'),
      path('agent_visit_requests/', views.agent_visit_requests, name='agent_visit_requests'),
      path('unassign_request/<int:visit_request_id>/', views.unassign_visit_request, name='unassign_visit_request'),
]
