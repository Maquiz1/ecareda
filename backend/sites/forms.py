from django import forms
from sites.models import Site

class SiteForm(forms.ModelForm):
    class Meta:
        model = Site
        fields = ['name', 'code', 'country', 'is_active']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter site name'}),
            'code': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter site code'}),
            'country': forms.Select(attrs={'class': 'form-select'}),
            'is_active': forms.CheckboxInput(attrs={'class': 'form-check-input ms-1'})
        }
