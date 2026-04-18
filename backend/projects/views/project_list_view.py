from django.shortcuts import render
from django.views.generic import ListView, CreateView
from django.urls import reverse_lazy
from projects.models import Project
from django.contrib.auth.mixins import LoginRequiredMixin

class ProjectListView(LoginRequiredMixin, ListView):
    model = Project
    template_name = "projects/project_list.html"
    context_object_name = "projects"

    def get_queryset(self):
        org_id = self.request.session.get("org_id")
        if org_id:
            return Project.objects.filter(organization_id=org_id)
        return Project.objects.none()
