from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from centers.models import Center
from centers.forms import CenterForm

def center_form(request, pk=None):
    if pk:
        center = get_object_or_404(Center, pk=pk)
        action_title = "Edit Center"
        action_button = "Save Changes"
        success_message = "Center updated successfully."
    else:
        center = None
        action_title = "Add New Center"
        action_button = "Create Center"
        success_message = "Center created successfully."

    if request.method == "POST":
        form = CenterForm(request.POST, instance=center)
        if form.is_valid():
            saved_instance = form.save(commit=False)
            
            # Ensure organization_id is set before saving
            if not saved_instance.organization_id:
                org_id = request.session.get("org_id")
                if org_id:
                    saved_instance.organization_id = org_id
                else:
                    messages.error(request, "Failed to create center: No active organization selected.")
                    return redirect('centers:centers-list')
                    
            saved_instance.save()
            messages.success(request, success_message)
            return redirect('centers:center-detail', pk=saved_instance.pk)
    else:
        form = CenterForm(instance=center)

    context = {
        'form': form,
        'action_title': action_title,
        'action_button': action_button,
        'center': center
    }
    return render(request, 'centers/center_form.html', context)
