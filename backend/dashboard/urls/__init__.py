# dashboard/urls/__init__.py
from django.urls import path, include

app_name = "dashboard"

urlpatterns = [
    path("", include("dashboard.urls.dashboard_urls")),
]
