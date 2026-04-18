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
        "select-organization/",
        views.select_organization,
        name="select_organization",
    ),

    path(
        "set_project/<int:project_id>/",
        views.set_project,
        name="set_project",
    ),

    path(
        "set-country/<int:country_id>/",
        views.set_country,
        name="set_country",
    ),

    path(
        "set-site/<int:site_id>/",
        views.set_site,
        name="set_site",
    ),

]