# subjects/urls/subjects_urls.py

from django.urls import path
from subjects.views import SubjectListView, SubjectDetailView, SubjectCreateView

urlpatterns = [
    path("", SubjectListView.as_view(), name="subject_list"),
    path("detail/<int:pk>/", SubjectDetailView.as_view(), name="subject_detail"),
    path("create/", SubjectCreateView.as_view(), name="subject_create"),
]