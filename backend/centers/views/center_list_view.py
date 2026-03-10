from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, CreateView
from django.urls import reverse_lazy
from centers.models import Center

class CenterListView(LoginRequiredMixin,ListView):
    model = Center
    template_name = "centers/centers_list.html"
    context_object_name = "centers"
    
