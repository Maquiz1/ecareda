from django.shortcuts import render

def custom_500(request):
    return render(
        request,
        "core/errors/error_base.html",
        {
            "code": "500",
            "title": "Server Error",
            "message": "Something went wrong on our server."
        },
        status=500
    )