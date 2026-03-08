from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User


@admin.register(User)
class CustomUserAdmin(UserAdmin):

    list_display = (
        "username",
        "email",
        "organization",
        "site",
        "is_data_manager",
        "is_monitor",
        "is_pi",
        "is_coordinator",
        "is_staff",
    )

    list_filter = (
        "organization",
        "site",
        "is_data_manager",
        "is_monitor",
        "is_pi",
        "is_coordinator",
        "is_staff",
    )

    fieldsets = UserAdmin.fieldsets + (
        (
            "Organization Information",
            {
                "fields": (
                    "organization",
                    "site",
                )
            },
        ),
        (
            "Study Roles",
            {
                "fields": (
                    "is_data_manager",
                    "is_monitor",
                    "is_pi",
                    "is_coordinator",
                )
            },
        ),
    )

    add_fieldsets = UserAdmin.add_fieldsets + (
        (
            "Organization Information",
            {
                "fields": (
                    "organization",
                    "site",
                )
            },
        ),
        (
            "Study Roles",
            {
                "fields": (
                    "is_data_manager",
                    "is_monitor",
                    "is_pi",
                    "is_coordinator",
                )
            },
        ),
    )