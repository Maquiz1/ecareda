from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from branches.models.branch_model import Branch
from branches.forms import BranchForm

def branch_form(request, pk=None):
    if pk:
        branch = get_object_or_404(Branch, pk=pk)
        action_title = "Edit Branch"
        action_button = "Save Changes"
        success_message = "Branch updated successfully."
    else:
        branch = None
        action_title = "Add New Branch"
        action_button = "Create Branch"
        success_message = "Branch created successfully."

    if request.method == "POST":
        form = BranchForm(request.POST, instance=branch)
        if form.is_valid():
            new_branch = form.save(commit=False)
            
            # Inject organization from session or user profile (multi-tenancy)
            if not new_branch.organization_id:
                org_id = request.session.get('org_id')
                if not org_id and hasattr(request.user, 'organization'):
                    org_id = request.user.organization.id
                
                if org_id:
                    new_branch.organization_id = org_id
            
            new_branch.save()
            messages.success(request, success_message)
            return redirect('branches:branch-detail', pk=new_branch.pk)
    else:
        form = BranchForm(instance=branch)

    context = {
        'form': form,
        'action_title': action_title,
        'action_button': action_button,
        'branch': branch
    }
    return render(request, 'branches/branch_form.html', context)
