from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView

from ..models import Country
from ..forms import CountryForm


class CountryCreateView(CreateView):

    model = Country
    form_class = CountryForm
    template_name = "countries/country_form.html"

    def get_success_url(self):
        return reverse_lazy("countries:countries-list")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["cancel_url"] = reverse_lazy("countries:countries-list")
        return context


class CountryUpdateView(UpdateView):

    model = Country
    form_class = CountryForm
    template_name = "countries/country_form.html"

    def get_success_url(self):
        return reverse_lazy("countries:countries-list")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["cancel_url"] = reverse_lazy("countries:countries-list")
        return context