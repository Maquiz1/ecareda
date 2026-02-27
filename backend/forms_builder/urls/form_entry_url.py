from django.urls import path
from forms_builder.views import FormEntryView

urlpatterns = [
    path("<int:pk>/entry/", FormEntryView.as_view(), name="form_entry"),
]