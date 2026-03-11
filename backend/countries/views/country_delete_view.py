from django.urls import reverse_lazy
from django.views.generic import DeleteView
from ..models import Country

class CountryDeleteView(DeleteView):
    model = Country
    template_name = "countries/country_confirm_delete.html"
    success_url = reverse_lazy("countries:countries-list")
