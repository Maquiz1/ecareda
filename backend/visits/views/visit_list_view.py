from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import DetailView, ListView
from visits.models import Visit
from forms_builder.models import FormResponse


class VisitListView(LoginRequiredMixin, ListView):
    model = Visit
    template_name = "visits/visit_list.html"
    context_object_name = "visits"
    
    def get_queryset(self):
        return (
            Visit.objects
            # .filter(is_deleted=False)
            # .select_related("site", "project")
            .order_by("subject_id")
        )
