# subjects/urls/__init__.py
from django.urls import path, include

app_name = "subjects"

urlpatterns = [
    path("", include("subjects.urls.subjects_urls")),
]
