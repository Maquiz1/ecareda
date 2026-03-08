from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect, get_object_or_404
from django.contrib import messages
from django.views import View

from subjects.models import Subject
from core.mixins import TenantQuerysetMixin


class SubjectDeleteView(LoginRequiredMixin, TenantQuerysetMixin, View):

    def post(self, request, pk):
        subject = get_object_or_404(self.get_queryset(), pk=pk)

        subject.is_deleted = True
        subject.save()

        messages.success(request, "Subject deleted successfully.")

        return redirect("subjects:subject_list")