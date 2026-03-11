# config/urls.py

from django.contrib import admin
from django.urls import path,include
from django.views.generic import RedirectView

admin.site.site_header = "e-Careda Administarions"
admin.site.site_title = "e-Careda Administarions"
admin.site.index_title = "Welcome to e-Careda Administarions Panel"

urlpatterns = [
    path("", RedirectView.as_view(url="/dashboard/")),
    path("dashboard/", include("dashboard.urls")),
    path("subjects/", include("subjects.urls")),
    path("visits/", include("visits.urls")),
    path("forms/", include("forms_builder.urls")),
    
    # Management
    path("countries/", include("countries.urls")),
    path("organizations/", include("organizations.urls")),
    path("branches/", include("branches.urls")),
    path("centers/", include("centers.urls")),
    # path("centres/", include("centres.urls")),
    path("projects/", include("projects.urls")),
    path("sites/", include("sites.urls")),
    
    # 🔐 Django built-in auth URLs
    path("accounts/", include("accounts.urls")),
    
    path('admin/', admin.site.urls),
]
