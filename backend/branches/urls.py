from django.urls import path

from branches.views import BranchListView,BranchDetailView


app_name = "branches"

urlpatterns = [
    path("", BranchListView.as_view(), name="branches-list"),
    path("<int:pk>/", BranchDetailView.as_view(), name="branch-detail"),
    # path("create/", ProjectCreateView.as_view(), name="project_create"),
]