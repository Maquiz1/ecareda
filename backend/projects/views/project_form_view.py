from django.shortcuts import render
from django.views.generic import CreateView
from django.urls import reverse_lazy
from projects.models.projects_model import Project

class ProjectCreateUpdateView(CreateView):
    model = Project
    template_name = "projects/project_form.html"
    context_object_name = "projects"
    
