from django.shortcuts import render
from django.views.generic import CreateView
from django.urls import reverse_lazy
from sites.models import Site

class SiteCreateUpdateView(CreateView):
    model = Site
    template_name = "sites/site_form.html"
    context_object_name = "project_sites"
    
