from django import forms
from branches.models.branch_model import Branch

class BranchForm(forms.ModelForm):
    class Meta:
        model = Branch
        fields = ['name', 'code', 'is_active']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter branch name'}),
            'code': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter branch code'}),
            'is_active': forms.CheckboxInput(attrs={'class': 'form-check-input ms-1'})
        }
