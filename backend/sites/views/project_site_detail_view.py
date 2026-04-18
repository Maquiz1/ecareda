from django.shortcuts import render
from django.views.generic import DetailView
from django.urls import reverse_lazy
from sites.models import Site
from django.contrib.auth.mixins import LoginRequiredMixin

class SiteDetailView(DetailView):
    model = Site
    template_name = "sites/site_detail.html"
    context_object_name = "site"

    def get_queryset(self):
        org_id = self.request.session.get("org_id")
        if org_id:
            return Site.objects.filter(organization_id=org_id)
        return Site.objects.none()

