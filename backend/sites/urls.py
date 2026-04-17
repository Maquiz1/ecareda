from django.urls import path

from sites.views import SiteListView, SiteDetailView, site_form

app_name = "sites"

urlpatterns = [
    path("", SiteListView.as_view(), name="site-list"),
    path("create/", site_form, name="site-create"),
    path("<int:pk>/", SiteDetailView.as_view(), name="site-detail"),
    path("<int:pk>/edit/", site_form, name="site-edit"),
]