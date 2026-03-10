from django.shortcuts import render
from django.views.generic import ListView, CreateView
from django.urls import reverse_lazy
from branches.models import Branch

class BranchListView(ListView):
    model = Branch
    template_name = "branches/branches_list.html"
    context_object_name = "branches"
    
