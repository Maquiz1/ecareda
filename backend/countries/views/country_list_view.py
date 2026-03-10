from django.shortcuts import render
from django.views.generic import ListView, CreateView
from django.urls import reverse_lazy
from countries.models import Country

class countryListView(ListView):
    model = Country
    template_name = "countries/country_list.html"
    context_object_name = "countries"
    
