from django import forms
from visits.models import Visit


class VisitForm(forms.ModelForm):
    class Meta:
        model = Visit
        fields = ["visit_type", "visit_number", "visit_date", "notes"]