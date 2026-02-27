from django.views.generic import CreateView
from django.urls import reverse_lazy
from visits.forms import VisitForm
from visits.models import Visit

class VisitCreateView(CreateView):
    model = Visit
    form_class = VisitForm
    template_name = "visits/visit_form.html"

    def form_valid(self, form):
        form.instance.subject_id = self.kwargs["subject_id"]
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy("subject_detail", kwargs={"pk": self.kwargs["subject_id"]})