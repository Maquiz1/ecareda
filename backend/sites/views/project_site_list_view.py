from django.shortcuts import render
from django.views.generic import ListView, CreateView
from django.urls import reverse_lazy
from sites.models import Site
from django.contrib.auth.mixins import LoginRequiredMixin

class SiteListView(ListView):
    model = Site
    template_name = "sites/site_list.html"
    context_object_name = "sites"
    
    def get_queryset(self):
        return (
            Site.objects
            # .filter(is_deleted=False)
            # .select_related("site", "project")
            .order_by("project","name")
        )
    
