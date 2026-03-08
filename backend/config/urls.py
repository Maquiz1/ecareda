# config/urls.py

from django.contrib import admin
from django.urls import path,include
from django.views.generic import RedirectView

urlpatterns = [
    path("", RedirectView.as_view(url="/dashboard/")),
    path("dashboard/", include("dashboard.urls")),
    path("subjects/", include("subjects.urls")),
    path("visits/", include("visits.urls")),
    path("forms/", include("forms_builder.urls")),
    path("projects/", include("projects.urls")),
    
    # 🔐 Django built-in auth URLs
    path("accounts/", include("accounts.urls")),
    
    path('admin/', admin.site.urls),
]
