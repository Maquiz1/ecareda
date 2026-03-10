from django.urls import path

from sites.views import SiteListView, SiteDetailView

app_name = "sites"

urlpatterns = [
    path("", SiteListView.as_view(), name="site-list"),
    path("<int:pk>/", SiteDetailView.as_view(), name="site-detail"),
    # path("create/", ProjectCreateView.as_view(), name="project_create"),
]