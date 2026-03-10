from django.shortcuts import render
from django.views.generic import DetailView
from django.urls import reverse_lazy
from sites.models import Site
    
class ProjectSiteDetailView(DetailView):
    model = Site
    template_name = "sites/project_site_detail.html"
    context_object_name = "site"
