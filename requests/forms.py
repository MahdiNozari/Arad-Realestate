from django import forms
from .models import ExpertiseRequest

class ExpertiseRequestForm(forms.ModelForm):
    class Meta:
        model = ExpertiseRequest
        fields = ['property_title', 'property_type', 'description']
        widgets = {
            'description': forms.Textarea(attrs={'rows': 3}),
        }
    
    expertise_fee = forms.DecimalField(initial=500, disabled=True)