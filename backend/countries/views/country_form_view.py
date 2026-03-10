from django.shortcuts import render
from django.views.generic import CreateView
from django.urls import reverse_lazy
from countries.models import Country
from django.contrib.auth.mixins import LoginRequiredMixin

class CountryCreateUpdateView(CreateView):
    model = Country
    template_name = "countries/country_form.html"
    context_object_name = "country"
    
