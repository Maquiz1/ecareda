from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, CreateView
from django.urls import reverse_lazy
from branches.models import Branch

class BranchListView(LoginRequiredMixin, ListView):
    model = Branch
    template_name = "branches/branches_list.html"
    context_object_name = "branches"

    def get_queryset(self):
        org_id = self.request.session.get("org_id")
        if org_id:
            return Branch.objects.filter(organization_id=org_id)
        return Branch.objects.none()
