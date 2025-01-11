from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.contenttypes.models import ContentType
from .models import VisitRequestCart, VisitRequest
from home.models import Villa, Land, Store, Apartment, Garden
from django.views import View
from accounts.models import Customer
from .forms import ExpertiseRequestForm,ExpertiseRequest


@login_required
def add_to_visit_cart(request, model_name, property_title):
    # انتخاب مدل مناسب براساس نام آن
    model_map = {
        'Apartment': Apartment,
        'Land': Land,
        'Villa': Villa,
        'Store': Store,
        'Garden': Garden,
    }

    model = model_map.get(model_name)
    if not model:
        messages.error(request, "مدل نامعتبر است!")
        return redirect('home:home')

    
    property_instance = get_object_or_404(model, title=property_title)

 
    if not isinstance(request.user, Customer):
        messages.error(request,'agent cant request to visit','danger')
        return redirect('home:home')
    else:
        visit_cart, created = VisitRequestCart.objects.get_or_create(user=request.user)

   
    content_type = ContentType.objects.get_for_model(model)
    existing_request = visit_cart.requests.filter(
        content_type=content_type,
        object_id=property_instance.id
    ).exists()

    if existing_request:
        messages.warning(request, "این ملک قبلاً به سبد بازدید شما اضافه شده است.")
        return redirect(f'home:{str(model_name).lower()}-list')

    else:
        VisitRequest.objects.create(
            cart=visit_cart,
            content_type=content_type,
            object_id=property_instance.id,  
        )
        messages.success(request, f"{property_instance.title} به سبد بازدید شما اضافه شد!")
        return redirect('requests:all_requests')


@login_required
def visit_cart(request):
    cart = VisitRequestCart.objects.get(user=request.user)
    return render(request, 'requests/visit_cart.html', {'cart': cart})

@login_required
def all_requests(request):
    # دریافت سبد خرید کاربر
    cart = VisitRequestCart.objects.get(user=request.user)
    
    requests = cart.requests.all()

    
    return render(request, 'requests/visit_cart.html', {'requests': requests})

def process_payment(request, request_id):
    # یافتن درخواست خاص
    visit_request = get_object_or_404(VisitRequest, id=request_id)
    
    # بررسی اگر درخواست قبلاً پرداخت نشده باشد
    if not visit_request.is_paid:
        visit_request.is_paid = True
        visit_request.status = 'in_progress'  # تغییر وضعیت به در حال انجام
        visit_request.save()
        
        messages.success(request, "پرداخت با موفقیت انجام شد! درخواست به حالت در حال انجام تغییر کرد.")
    else:
        messages.info(request, "این درخواست قبلاً پرداخت شده است.")

    return redirect('requests:all_requests')


@login_required
def remove_visit_request(request, request_id):
    # یافتن درخواست بازدید خاص
    visit_request = get_object_or_404(VisitRequest, id=request_id, cart__user=request.user)

    # حذف درخواست از سبد خرید
    visit_request.delete()

    # نمایش پیام موفقیت
    messages.success(request, "درخواست بازدید با موفقیت از سبد خرید شما حذف شد.")
    return redirect('requests:all_requests')  # هدایت به صفحه درخواست‌ها

class RequestExpertiseView(View):
    def get(self, request):
        form = ExpertiseRequestForm()
        return render(request, 'requests/request_expertise.html', {'form': form})

    def post(self, request):
        form = ExpertiseRequestForm(request.POST)
        if form.is_valid():
            expertise_request = form.save(commit=False)
            expertise_request.user = request.user 
            expertise_request.save()
            messages.success(request, "درخواست کارشناسی ملک شما با موفقیت ارسال شد.")
            return redirect('home:home')
        return render(request, 'requests/request_expertise.html', {'form': form})
    

@login_required
def user_expertise_requests(request):
    expertise_requests = ExpertiseRequest.objects.filter(user=request.user)
    return render(request, 'requests/user_expertise_requests.html', {
        'expertise_requests': expertise_requests
    })
class PayExpertiseRequestView(View):
    def post(self, request, pk):
        expertise_request = get_object_or_404(ExpertiseRequest, pk=pk, user=request.user)
        if expertise_request.is_paid:
            messages.warning(request, "این درخواست قبلاً پرداخت شده است.")
            return redirect('requests:user_expertise_requests')

        
        expertise_request.is_paid = True
        expertise_request.status = 'in_progress'  
        expertise_request.save()

        messages.success(request, "پرداخت شما با موفقیت انجام شد. درخواست به وضعیت 'در انتظار کارشناسی' تغییر کرد.")
        return redirect('requests:user_expertise_requests')

@login_required
def remove_expertise_request(request, pk):
    expertise_request = get_object_or_404(ExpertiseRequest, pk=pk, user=request.user)

    if expertise_request.is_paid:
        messages.warning(request, "شما نمی‌توانید یک درخواست پرداخت شده را حذف کنید.")
        return redirect('requests:user_expertise_requests')

    expertise_request.delete()

    messages.success(request, "درخواست کارشناسی با موفقیت حذف شد.")
    return redirect('requests:expertise_requests')

from django.shortcuts import render, get_object_or_404, redirect
from .models import ExpertiseRequest
from django.contrib.auth.decorators import login_required

@login_required
def manage_expertise_requests(request):
    # دریافت درخواست‌هایی که هنوز ایجنتی برای آن‌ها تعیین نشده
    requests = ExpertiseRequest.objects.filter(expert_assigned__isnull=True)

    if request.method == 'POST':
        # دریافت درخواست و ایجنت انتخابی از فرم
        request_id = request.POST.get('request_id')
        action = request.POST.get('action')  # 'accept' یا 'delete'
        expertise_request = get_object_or_404(ExpertiseRequest, id=request_id)

        if action == 'accept':
            # انتخاب ایجنت (شما می‌توانید ایجنت را به صورت دستی یا خودکار انتخاب کنید)
            expertise_request.expert_assigned = request.user  # یا ایجنت مشخصی
            expertise_request.save()
        elif action == 'delete':
            expertise_request.delete()

        return redirect('requests:manage_expertise_requests')  # پس از انجام عملیات، صفحه به روز می‌شود

    return render(request, 'requests/manage_expertise_requests.html', {'requests': requests})

@login_required
def agent_expertise_requests(request):
    # دریافت درخواست‌های مربوط به ایجنت جاری
    requests = ExpertiseRequest.objects.filter(expert_assigned=request.user)
    return render(request, 'requests/agent_expertise_requests.html', {'requests': requests})


def expertise_request_details(request, request_id):
    # دریافت درخواست با id مشخص
    expertise_request = get_object_or_404(ExpertiseRequest, id=request_id)

    return render(request, 'requests/expertise_request_details.html', {'request': expertise_request})
# views.py

from django.shortcuts import get_object_or_404, redirect
from .models import ExpertiseRequest

def cancel_expertise_request(request, expertise_request_id):
    # گرفتن درخواست کارشناسی بر اساس ID
    expertise_request = get_object_or_404(ExpertiseRequest, id=expertise_request_id)
    
    # بررسی اینکه آیا کاربر ایجنت فعلی است یا خیر
    if expertise_request.expert_assigned == request.user:
        # لغو اختصاص ایجنت به درخواست
        expertise_request.expert_assigned = None
        expertise_request.save()

        # هدایت به صفحه مدیریت درخواست‌ها بعد از لغو
        return redirect('requests:manage_expertise_requests')
    else:
        # در صورتی که ایجنت جاری نباشد، دسترسی به لغو امکان‌پذیر نیست
        return redirect('requests:manage_expertise_requests')

# views.py

from django.shortcuts import get_object_or_404, redirect
from .models import ExpertiseRequest

def cancel_expertise_request(request, expertise_request_id):
    # گرفتن درخواست کارشناسی بر اساس ID
    expertise_request = get_object_or_404(ExpertiseRequest, id=expertise_request_id)

    # بررسی اینکه آیا کاربر (ادمین) اجازه لغو انتخاب را دارد
    if expertise_request.expert_assigned == request.user:
        # لغو اختصاص ایجنت به درخواست (بازگشت به حالت بدون کارشناس)
        expertise_request.expert_assigned = None
        expertise_request.save()

        # هدایت به صفحه مدیریت درخواست‌ها بعد از لغو
        return redirect('requests:manage_expertise_requests')
    else:
        # در صورتی که ایجنت جاری نباشد، دسترسی به لغو امکان‌پذیر نیست
        return redirect('requests:manage_expertise_requests')
from django.shortcuts import render, get_object_or_404, redirect
from .models import VisitRequest

# مشاهده درخواست‌های بازدید موجود برای ایجنت
def available_visit_requests(request):
    requests = VisitRequest.objects.filter(request_assigned__isnull=True)
    return render(request, 'requests/available_requests.html', {'requests': requests})

# تخصیص درخواست بازدید به ایجنت
def assign_visit_request(request, visit_request_id):
    visit_request = get_object_or_404(VisitRequest, id=visit_request_id)
    visit_request.request_assigned = request.user  # فرض بر این است که ایجنت به کاربر فعلی مرتبط است
    visit_request.save()
    return redirect('requests:available_visit_requests')

# حذف درخواست بازدید
def delete_visit_request(request, visit_request_id):
    visit_request = get_object_or_404(VisitRequest, id=visit_request_id)
    visit_request.delete()
    return redirect('requests:available_visit_requests')

# مشاهده درخواست‌های بازدید متعلق به ایجنت
def agent_visit_requests(request):
    requests = VisitRequest.objects.filter(request_assigned=request.user)
    return render(request, 'requests/agent_requests.html', {'requests': requests})

# لغو تخصیص درخواست بازدید
def unassign_visit_request(request, visit_request_id):
    visit_request = get_object_or_404(VisitRequest, id=visit_request_id)
    if visit_request.request_assigned == request.user:
        visit_request.request_assigned = None
        visit_request.save()
    return redirect('requests:available_visit_requests')
