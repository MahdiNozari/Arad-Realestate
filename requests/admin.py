from django.contrib import admin
from .models import VisitRequest, VisitRequestCart,ExpertiseRequest
from accounts.custom_admin import custom_admin_site

# Inline برای نمایش VisitRequest‌ها در VisitRequestCart
class VisitRequestInline(admin.TabularInline):
    model = VisitRequest
    extra = 0  
    readonly_fields = ('content_type', 'object_id', 'file', 'created_at') 
    can_delete = True  

# مدیریت VisitRequestCart

class VisitRequestCartAdmin(admin.ModelAdmin):
    list_display = ('user',) 
    search_fields = ('user__name',)  
    inlines = [VisitRequestInline]  
custom_admin_site.register(VisitRequestCart,VisitRequestCartAdmin)
# مدیریت VisitRequest

class VisitRequestAdmin(admin.ModelAdmin):
    list_display = ('cart', 'property_type', 'property_title', 'created_at')
    list_filter = ('content_type', 'created_at')  # فیلتر بر اساس نوع ملک و تاریخ ایجاد
    search_fields = ('cart__user__username', 'object_id')  # جستجو بر اساس کاربر و شناسه ملک
    readonly_fields = ('content_type', 'object_id', 'created_at')  # فیلدهای فقط خواندنی

    # فقط درخواست‌های پرداخت‌شده را در ادمین نمایش بده
    def get_queryset(self, request):
        qs = super().get_queryset(request)
        return qs.filter(is_paid=True)

    
    def property_type(self, obj):
        return obj.content_type.name  
    property_type.short_description = "نوع ملک"

   
    def property_title(self, obj):
        
        return str(obj.file)
    property_title.short_description = "عنوان ملک"
custom_admin_site.register(VisitRequest,VisitRequestAdmin)

class ExpertiseRequestAdmin(admin.ModelAdmin):
    list_display = ('property_title', 'user', 'status', 'expertise_fee', 'is_paid', 'created_at')
    list_filter = ('is_paid', 'status') 
    search_fields = ('property_title', 'user__username') 

    def get_queryset(self, request):
        queryset = super().get_queryset(request)
        return queryset.filter(is_paid=True)

custom_admin_site.register(ExpertiseRequest, ExpertiseRequestAdmin)