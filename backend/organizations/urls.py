from django.urls import path

from organizations.views import OrganizationsListView,OrganizationsDetailView


app_name = "organizations"

urlpatterns = [
    path("", OrganizationsListView.as_view(), name="organizations-list"),
    path("<int:pk>/", OrganizationsDetailView.as_view(), name="organization-detail"),
    # path("create/", ProjectCreateView.as_view(), name="project_create"),
]