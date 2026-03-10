from django.shortcuts import render
from django.views.generic import DetailView
from django.urls import reverse_lazy
from sites.models import Site
    
class SiteDetailView(DetailView):
    model = Site
    template_name = "sites/site_detail.html"
    context_object_name = "site"
