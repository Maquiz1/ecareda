from django.shortcuts import render
from django.views.generic import DetailView
from django.urls import reverse_lazy
from branches.models import Branch

class BranchDetailView(DetailView):
    model = Branch
    template_name = "branches/branch_detail.html"
    context_object_name = "branch"
    
