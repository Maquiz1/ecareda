# from django.shortcuts import render
# from django.views.generic import CreateView
# from django.urls import reverse_lazy
# from countries.models import Country
# from django.contrib.auth.mixins import LoginRequiredMixin

# class CountryCreateUpdateView(CreateView):
#     model = Country
#     template_name = "countries/country_form.html"
#     context_object_name = "country"
    

from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView

from ..models import Country
from ..forms import CountryForm

class CountryCreateView(CreateView):
    model = Country
    form_class = CountryForm
    template_name = "countries/country_form.html"
    success_url = reverse_lazy("countries:countries-list")


class CountryUpdateView(UpdateView):
    model = Country
    form_class = CountryForm
    template_name = "countries/country_form.html"
    success_url = reverse_lazy("countries:countries-list")

