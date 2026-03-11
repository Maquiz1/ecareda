from django.core.paginator import Paginator
from django.shortcuts import render
from organizations.models import Organization


def organization_list(request):

    q = request.GET.get("q")

    organizations = Organization.objects.all().order_by("name")

    if q:
        organizations = organizations.filter(name__icontains=q)

    paginator = Paginator(organizations, 10)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)

    rows = ""

    for i, org in enumerate(page_obj, start=1):

        rows += f"""
        <tr>
            <td>{i}</td>
            <td><strong>{org.name}</strong></td>
            <td><span class="badge bg-info text-dark">{org.code}</span></td>
            <td>{org.created_at:%Y-%m-%d}</td>
            <td class="text-end">
                <a href="/organizations/{org.id}/"
                   class="btn btn-sm btn-outline-primary">
                   <i class="fa fa-eye"></i> View
                </a>
            </td>
        </tr>
        """

    return render(
        request,
        "organizations/organizations_list.html",
        {
            "organizations": organizations,
            "table_rows": rows,
            "page_obj": page_obj,
        },
    )