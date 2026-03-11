from django import forms
from ..models import Country

class CountryForm(forms.ModelForm):

    class Meta:
        model = Country
        fields = [
            "organization",
            "name",
            "code",
            "iso_code",
            "is_active",
        ]

        widgets = {

            "organization": forms.Select(
                attrs={"class": "form-select"}
            ),

            "name": forms.TextInput(
                attrs={"class": "form-control"}
            ),

            "code": forms.TextInput(
                attrs={"class": "form-control"}
            ),

            "iso_code": forms.TextInput(
                attrs={"class": "form-control"}
            ),

            "is_active": forms.CheckboxInput(
                attrs={"class": "form-check-input"}
            ),
        }
