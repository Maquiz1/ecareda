from django.urls import path
from visits.views import VisitDetailView,VisitCreateView


urlpatterns = [
    path("<int:pk>/", VisitDetailView.as_view(), name="visit_detail"),
    path("create/<int:subject_id>/", VisitCreateView.as_view(), name="visit_create"),
]