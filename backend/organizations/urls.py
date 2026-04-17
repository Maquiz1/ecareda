from django.urls import path

from organizations.views import OrganizationsListView, OrganizationsDetailView, organization_form


app_name = "organizations"

urlpatterns = [
    path("", OrganizationsListView.as_view(), name="organizations-list"),
    path("create/", organization_form, name="organization-create"),
    path("<int:pk>/", OrganizationsDetailView.as_view(), name="organization-detail"),
    path("<int:pk>/edit/", organization_form, name="organization-edit"),
]