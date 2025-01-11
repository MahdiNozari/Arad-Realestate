from django.core.mail import send_mail
from django.conf import settings

def send_otp_code(email, code):
    subject = "Your OTP Code"
    message = f"Your OTP code is: {code}. Please use this code to verify your identity."
    email_from = settings.DEFAULT_FROM_EMAIL
    recipient_list = [email]
    
    try:
        send_mail(subject, message, email_from, recipient_list)
        return True
    except Exception as e:
        print(f"Error sending email: {e}")
        return False
