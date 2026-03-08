from django.urls import path
from visits.views import VisitListView,VisitDetailView,VisitCreateView

app_name = "visits"

urlpatterns = [
    path("", VisitListView.as_view(), name="visit_list"),
    path("<int:pk>/", VisitDetailView.as_view(), name="visit_detail"),
    path("create/<int:subject_id>/", VisitCreateView.as_view(), name="visit_create"),
]