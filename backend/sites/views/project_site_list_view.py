from django.shortcuts import render
from django.views.generic import ListView, CreateView
from django.urls import reverse_lazy
from sites.models import Site
from django.contrib.auth.mixins import LoginRequiredMixin

class SiteListView(LoginRequiredMixin, ListView):
    model = Site
    template_name = "sites/site_list.html"
    context_object_name = "sites"
    
    def get_queryset(self):
        org_id = self.request.session.get("org_id")
        country_id = self.request.session.get("country_id")
        
        qs = Site.objects.all()
        
        if org_id:
            qs = qs.filter(organization_id=org_id)
        if country_id:
            qs = qs.filter(country_id=country_id)
            
        return qs.order_by("name")
