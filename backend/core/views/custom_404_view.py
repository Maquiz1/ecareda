from django.shortcuts import render

def custom_404(request, exception):
    return render(
        request,
        "core/errors/error_base.html",
        {
            "code": "404",
            "title": "Page Not Found",
            "message": "The page you are looking for does not exist."
        },
        status=404
    )