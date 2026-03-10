from django.urls import path
from centers.views import CenterListView,CenterDetailView

app_name = "centers"

urlpatterns = [
    path("", CenterListView.as_view(), name="centers-list"),
    path("<int:pk>/", CenterDetailView.as_view(), name="center-detail"),
    # path("create/", ProjectCreateView.as_view(), name="project_create"),
]