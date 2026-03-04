from django import forms
from subjects.models import Subject
from projects.models import Project
from sites.models import Site

# class SubjectForm(forms.ModelForm):
#     class Meta:
#         model = Subject
#         fields = ["subject_id", "project"]
        
        
class SubjectForm(forms.ModelForm):

    class Meta:
        model = Subject
        fields = ["project", "site", "subject_id", "enrollment_date"]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # force queryset evaluation
        self.fields["project"].queryset = Project.objects.all().order_by("name")
        self.fields["site"].queryset = Site.objects.all().order_by("name")