from django.contrib.auth.backends import BaseBackend
from .models import Customer

class CustomerBackend(BaseBackend):
    def authenticate(self, request, email=None, password=None, **kwargs):
        try:
            customer = Customer.objects.get(email=email)
            if customer.check_password(password):
                print(customer)
                return customer
        except Customer.DoesNotExist:
            return None

    def get_user(self, user_id):
        try:
            return Customer.objects.get(pk=user_id)
        except Customer.DoesNotExist:
            return None

