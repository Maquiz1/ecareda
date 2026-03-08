# dashboard/urls/dashboard_urls.py

from django.urls import path
from dashboard.views import DashBoardView

urlpatterns = [
    path("", DashBoardView.as_view(), name="dashboard"),
]