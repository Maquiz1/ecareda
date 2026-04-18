from django.shortcuts import redirect
from sites.models import Site

def set_site(request, site_id):
    request.session["site_id"] = site_id
    return redirect(request.META.get("HTTP_REFERER", "/"))
