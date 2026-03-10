from django.shortcuts import render
from django.views.generic import ListView, CreateView
from django.urls import reverse_lazy
from projects.models.projects_model import Project

class ProjectListView(ListView):
    model = Project
    template_name = "projects/project_list.html"
    context_object_name = "projects"
    
