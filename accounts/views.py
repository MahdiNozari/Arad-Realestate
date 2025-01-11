from django.shortcuts import render,redirect
from django.views import View
from.forms import RegisterForm,VerifyForm,LoginForm
from django.contrib import messages
from .models import OtpCode,Customer,Agent,User
from datetime import datetime, timedelta
from django.utils import timezone
from django.contrib.auth import login,authenticate,logout
from .backends import CustomerBackend
from utils import send_otp_code
import random
from requests.models import VisitRequestCart
from django.views.decorators.csrf import csrf_exempt

class RegisterView(View):
    form_class = RegisterForm

    def get(self, request):
        form = self.form_class()
        return render(request, 'accounts/register.html', {'form': form})

    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            random_code = random.randint(1000, 9999)
            send_otp_code(form.cleaned_data['email'], random_code)
            OtpCode.objects.create(email=form.cleaned_data['email'], code=random_code)

            request.session['user_registeration_info'] = {
                'phone': form.cleaned_data['phone'],
                'email': form.cleaned_data['email'],
                'name': form.cleaned_data['fullname'],
                'password': form.cleaned_data['password2'],
            }
            request.session.modified = True
            messages.success(request, 'منتظر تایید کد باشید.', 'success')
            return redirect('accounts:verify_code')

        return redirect('home:home')  # یا یک صفحه ثبت‌نام با پیام خطا

class RegisterVerifyCodeView(View):
    form_class = VerifyForm

    def get(self, request):
        form = self.form_class
        return render(request, 'accounts/verify.html', {'form': form})

    def post(self, request):
        user_session = request.session.get('user_registeration_info')
        if not user_session:
            messages.error(request, 'Session expired. Please register again.', 'danger')
            return redirect('accounts:register')

        try:
            
            code_instance = OtpCode.objects.get(email=user_session['email'])
        except OtpCode.DoesNotExist:
            messages.error(request, 'Verification code not found. Please register again.', 'danger')
            return redirect('accounts:register')

        form = self.form_class(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            if cd['code'] == code_instance.code:
                if code_instance.created + timedelta(minutes=2) >= timezone.now():
                   
                    user = Customer.objects.create_user(
                        name=user_session['name'],
                        email=user_session['email'],
                        phone=user_session['phone'],
                        password=user_session['password']
                    )
                    code_instance.delete()

                    
                    VisitRequestCart.objects.create(user=user)

                    messages.success(request, 'You registered successfully!', 'success')
                    return redirect('home:home')
                else:
                    messages.error(request, 'The verification code has expired.', 'danger')
                    code_instance.delete()
            else:
                messages.error(request, 'The verification code is invalid.', 'danger')
                return redirect('accounts:verify_code')

        return render(request, 'accounts/verify.html', {'form': form})

class LoginView(View):
    form_class = LoginForm
    template_name = 'accounts/login.html'
    

    def get(self, request):
        form = self.form_class
        return render(request, self.template_name, {'form': form})

    def post(self,request):
        form=self.form_class(request.POST) 
        if form.is_valid():
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            customer =authenticate(request, email=email, password=password)
            if customer:
                login(request, customer)
                messages.success(request,'you login to site successfully', 'success')
                return redirect('home:home')
            else:
                messages.error(request, 'invalid email or password', 'danger')
                return redirect('accounts:login')
            
        return render(request, 'accounts/login.html')

    
class LogoutView(View):
    def get(self, request):
        logout(request)
        messages.success(request, 'you logged out successfully', 'success')
        return redirect('accounts:login')