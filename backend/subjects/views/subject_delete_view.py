from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.contrib import messages
from django.views.generic import DeleteView

from subjects.models import Subject
from core.mixins import TenantQuerysetMixin


class SubjectDeleteView(LoginRequiredMixin, TenantQuerysetMixin, DeleteView):

    model = Subject
    success_url = reverse_lazy("subjects:subject_list")

    def delete(self, request, *args, **kwargs):
        self.object = self.get_object()

        # Soft delete
        self.object.delete()

        messages.success(request, "Subject deleted successfully.")

        return redirect(self.success_url)