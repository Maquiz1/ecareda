
from django.views import View
from django.shortcuts import render, redirect, get_object_or_404
from forms_builder.models import FormResponse, FieldValue
from django.utils import timezone
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import CreateView, ListView
    

class FormListView(LoginRequiredMixin, ListView):
    model = FormResponse
    template_name = "forms_builder/form_builder_list.html"
    context_object_name = "forms"