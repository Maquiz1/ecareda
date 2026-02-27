from django import forms
from subjects.models import Subject


class SubjectForm(forms.ModelForm):
    class Meta:
        model = Subject
        fields = ["subject_id", "project"]