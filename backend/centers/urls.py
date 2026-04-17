from django.urls import path
from centers.views import CenterListView, CenterDetailView, center_form

app_name = "centers"

urlpatterns = [
    path("", CenterListView.as_view(), name="centers-list"),
    path("create/", center_form, name="center-create"),
    path("<int:pk>/", CenterDetailView.as_view(), name="center-detail"),
    path("<int:pk>/edit/", center_form, name="center-edit"),
]