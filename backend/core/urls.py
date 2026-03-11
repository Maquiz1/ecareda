handler404 = "core.views.custom_404"
handler500 = "core.views.custom_500"


from django.urls import path
from . import views

app_name = "core"

urlpatterns = [

    path(
        "set-organization/<int:org_id>/",
        views.set_organization,
        name="set_organization",
    ),

    path(
        "set-project/<int:project_id>/",
        views.set_project,
        name="set_project",
    ),

]