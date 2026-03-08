from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView
from subjects.models import Subject

class DashBoardView(LoginRequiredMixin, ListView):
    model = Subject
    template_name = "dashboard/dashboard.html"
    context_object_name = "dashboard_subjects"

    def get_queryset(self):
        return Subject.objects.filter(is_deleted=False)


    
