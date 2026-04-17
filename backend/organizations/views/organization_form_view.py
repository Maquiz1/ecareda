from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from organizations.models import Organization
from organizations.forms import OrganizationForm

def organization_form(request, pk=None):
    if pk:
        organization = get_object_or_404(Organization, pk=pk)
        action_title = "Edit Organization"
        action_button = "Save Changes"
        success_message = "Organization updated successfully."
    else:
        organization = None
        action_title = "Add New Organization"
        action_button = "Create Organization"
        success_message = "Organization created successfully."

    if request.method == "POST":
        form = OrganizationForm(request.POST, instance=organization)
        if form.is_valid():
            saved_instance = form.save()
            messages.success(request, success_message)
            return redirect('organizations:organization-detail', pk=saved_instance.pk)
    else:
        form = OrganizationForm(instance=organization)

    context = {
        'form': form,
        'action_title': action_title,
        'action_button': action_button,
        'organization': organization
    }
    return render(request, 'organizations/organization_form.html', context)
