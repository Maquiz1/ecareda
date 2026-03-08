# subjects/forms/subject_form.py

from django import forms
from subjects.models import Subject
from projects.models import Project
from sites.models import Site
from core.forms.tenant_model_form import TenantModelForm

class SubjectForm(TenantModelForm):

    class Meta:
        model = Subject
        fields = ["project", "site", "subject_id", "enrollment_date"]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields["project"].queryset = Project.objects.all().order_by("name")
        self.fields["site"].queryset = Site.objects.all().order_by("name")

        self.fields["enrollment_date"].widget.attrs["type"] = "date"