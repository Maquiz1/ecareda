from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from sites.models import Site
from sites.forms import SiteForm

def site_form(request, pk=None):
    if pk:
        site = get_object_or_404(Site, pk=pk)
        action_title = "Edit Site"
        action_button = "Save Changes"
        success_message = "Site updated successfully."
    else:
        site = None
        action_title = "Add New Site"
        action_button = "Create Site"
        success_message = "Site created successfully."

    if request.method == "POST":
        form = SiteForm(request.POST, instance=site)
        if form.is_valid():
            # Handle organization_id for multi-tenancy as in other modules
            new_site = form.save(commit=False)
            
            # Inject organization from session if not set (standard pattern in this app)
            if not new_site.organization_id:
                org_id = request.session.get('org_id')
                if not org_id and hasattr(request.user, 'organization'):
                    org_id = request.user.organization.id
                
                if org_id:
                    new_site.organization_id = org_id
            
            new_site.save()
            messages.success(request, success_message)
            return redirect('sites:site-detail', pk=new_site.pk)
    else:
        form = SiteForm(instance=site)

    context = {
        'form': form,
        'action_title': action_title,
        'action_button': action_button,
        'site': site
    }
    return render(request, 'sites/site_form.html', context)
