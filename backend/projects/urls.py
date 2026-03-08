from django.urls import path

from projects.views import ProjectListView, ProjectDetailView

app_name = "projects"

urlpatterns = [
    path("", ProjectListView.as_view(), name="project_list"),
    path("<int:pk>/", ProjectDetailView.as_view(), name="project_detail"),
    # path("create/", ProjectCreateView.as_view(), name="project_create"),
]