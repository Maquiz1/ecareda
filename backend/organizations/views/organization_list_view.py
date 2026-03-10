from django.shortcuts import render
from django.views.generic import ListView, CreateView
from django.urls import reverse_lazy
from organizations.models import Organization

class OrganizationsListView(ListView):
    model = Organization
    template_name = "organizations/organizations_list.html"
    context_object_name = "organizations"
    
