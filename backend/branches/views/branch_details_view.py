from django.shortcuts import render
from django.views.generic import DetailView
from django.urls import reverse_lazy
from branches.models import Branch
from django.contrib.auth.mixins import LoginRequiredMixin

class BranchDetailView(DetailView):
    model = Branch
    template_name = "branches/branch_detail.html"
    context_object_name = "branch"

    def get_queryset(self):
        org_id = self.request.session.get("org_id")
        if org_id:
            return Branch.objects.filter(organization_id=org_id)
        return Branch.objects.none()
