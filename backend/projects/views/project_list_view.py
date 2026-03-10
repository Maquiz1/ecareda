from django.shortcuts import render
from django.views.generic import ListView, CreateView
from django.urls import reverse_lazy
from projects.models import Project
from django.contrib.auth.mixins import LoginRequiredMixin

class ProjectListView(ListView):
    model = Project
    template_name = "projects/project_list.html"
    context_object_name = "projects"
    
