from django.urls import path

from countries.views import countryListView, CountryDetailView,CountryCreateView,CountryUpdateView,CountryDeleteView

app_name = "countries"

urlpatterns = [
    path("", countryListView.as_view(), name="countries-list"),
    path("<int:pk>/", CountryDetailView.as_view(), name="country-detail"),
    # path("create/", ProjectCreateView.as_view(), name="project_create"),
    path( "create/", CountryCreateView.as_view(), name="country-create" ), 
    path( "<int:pk>/update/", CountryUpdateView.as_view(), name="country-update" ),
    path( "<int:pk>/delete/", CountryDeleteView.as_view(), name="country-delete" ),
]