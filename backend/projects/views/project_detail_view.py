from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView
from django.urls import reverse_lazy
from projects.models.projects_model import Project
    
class ProjectDetailView(DetailView):
    model = Project
    template_name = "projects/project_detail.html"
    context_object_name = "project"
