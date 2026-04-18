from django.urls import path

from branches.views import BranchListView, BranchDetailView, branch_form

app_name = "branches"

urlpatterns = [
    path("", BranchListView.as_view(), name="branches-list"),
    path("create/", branch_form, name="branch-create"),
    path("<int:pk>/", BranchDetailView.as_view(), name="branch-detail"),
    path("<int:pk>/edit/", branch_form, name="branch-edit"),
]