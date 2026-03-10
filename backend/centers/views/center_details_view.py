from django.shortcuts import render
from django.views.generic import DetailView
from django.urls import reverse_lazy
from centers.models import Center
from django.contrib.auth.mixins import LoginRequiredMixin

class CenterDetailView(DetailView):
    model = Center
    template_name = "centers/center_detail.html"
    context_object_name = "center"
    
