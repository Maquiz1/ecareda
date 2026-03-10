from django.shortcuts import render
from django.views.generic import DetailView
from django.urls import reverse_lazy
from countries.models import Country
from django.contrib.auth.mixins import LoginRequiredMixin
   
class CountryDetailView(DetailView):
    model = Country
    template_name = "countries/country_detail.html"
    context_object_name = "country"
