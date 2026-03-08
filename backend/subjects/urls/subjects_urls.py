from django.urls import path
from subjects.views import SubjectListView, SubjectDetailView,SubjectCreateView

app_name = "subjects"

urlpatterns = [
    path("", SubjectListView.as_view(), name="subject_list"),
    path("<int:pk>/", SubjectDetailView.as_view(), name="subject_detail"),
    path("create/", SubjectCreateView.as_view(), name="subject_create"),
]