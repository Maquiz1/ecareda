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

    context = {
        'form': None,
        'action_title': action_title,
        'action_button': action_button,
        'branch': branch
    }

    if request.method == "POST":
        form = BranchForm(request.POST, instance=branch)
        context['form'] = form
        if form.is_valid():
            new_branch = form.save(commit=False)
            
            # Inject organization from session or user profile (multi-tenancy)
            if not new_branch.organization_id:
                org_id = request.session.get('org_id')
                if not org_id:
                    user_org = getattr(request.user, 'organization', None)
                    if user_org:
                        org_id = user_org.id
                
                if org_id:
                    new_branch.organization_id = org_id
                else:
                    messages.error(request, "Error: No organization found for this user. Cannot create branch.")
                    return render(request, 'branches/branch_form.html', context)
            
            new_branch.save()
            messages.success(request, success_message)
            return redirect('branches:branch-detail', pk=new_branch.pk)
    else:
        form = BranchForm(instance=branch)
        context['form'] = form

    return render(request, 'branches/branch_form.html', context)
