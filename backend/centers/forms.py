from django import forms
from .models import Center

class CenterForm(forms.ModelForm):
    class Meta:
        model = Center
        fields = ['branch', 'name', 'code']
        widgets = {
            'branch': forms.Select(attrs={'class': 'form-select'}),
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter center name'}),
            'code': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter unique center code'}),
        }
