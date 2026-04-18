from django.shortcuts import redirect
from countries.models.countries_model import Country

def set_country(request, country_id):
    request.session["country_id"] = country_id
    # Reset site if country changes? (Optional)
    # request.session.pop("site_id", None)
    return redirect(request.META.get("HTTP_REFERER", "/"))
