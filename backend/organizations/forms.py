from django import forms
from .models import Organization

class OrganizationForm(forms.ModelForm):
    class Meta:
        model = Organization
        fields = ['name', 'code', 'description', 'is_active']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter organization name'}),
            'code': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter unique code'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Enter description...', 'rows': 4}),
            'is_active': forms.CheckboxInput(attrs={'class': 'form-check-input ms-1'})
        }
