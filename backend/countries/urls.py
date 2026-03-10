from django.urls import path

from countries.views import countryListView, CountryDetailView

app_name = "countries"

urlpatterns = [
    path("", countryListView.as_view(), name="countries-list"),
    path("<int:pk>/", CountryDetailView.as_view(), name="country-detail"),
    # path("create/", ProjectCreateView.as_view(), name="project_create"),
]