from django.shortcuts import render
from django.views.generic import DetailView
from django.urls import reverse_lazy
from organizations.models import Organization

class OrganizationsDetailView(DetailView):
    model = Organization
    template_name = "organizations/organizations_detail.html"
    context_object_name = "organization"
    
