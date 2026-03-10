from django.urls import path

from sites.views import ProjectSiteListView, ProjectSiteDetailView

app_name = "sites"

urlpatterns = [
    path("", ProjectSiteListView.as_view(), name="project-site-list"),
    path("<int:pk>/", ProjectSiteDetailView.as_view(), name="project-site-detail"),
    # path("create/", ProjectCreateView.as_view(), name="project_create"),
]