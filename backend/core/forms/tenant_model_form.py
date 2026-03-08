# core/forms/tenant_model_form.py

from django import forms

class TenantModelForm(forms.ModelForm):
    """
    Base form for tenant-aware models.
    - Restricts queryset fields to the user's organization
    - Automatically applies Bootstrap styling
    """

    def __init__(self, *args, **kwargs):

        self.request = kwargs.pop("request", None)

        super().__init__(*args, **kwargs)

        user = getattr(self.request, "user", None)

        for name, field in self.fields.items():

            # -----------------------------
            # 1️⃣ Tenant filtering
            # -----------------------------
            if hasattr(field, "queryset") and user:

                model = field.queryset.model

                if hasattr(model, "organization") and hasattr(user, "organization"):

                    field.queryset = field.queryset.filter(
                        organization=user.organization
                    )

            # -----------------------------
            # 2️⃣ Bootstrap styling
            # -----------------------------
            if isinstance(field.widget, forms.CheckboxInput):

                field.widget.attrs["class"] = "form-check-input"

            elif isinstance(field.widget, forms.Select):

                field.widget.attrs["class"] = "form-select"

            else:

                field.widget.attrs["class"] = "form-control"
                field.widget.attrs["placeholder"] = field.label
                
# class TenantModelForm(forms.ModelForm):
#     """
#     Restricts queryset fields to the user's organization.
#     """

#     def __init__(self, *args, **kwargs):

#         self.request = kwargs.pop("request", None)

#         super().__init__(*args, **kwargs)

#         if not self.request:
#             return

#         user = self.request.user

#         for field in self.fields.values():

#             if hasattr(field, "queryset"):

#                 model = field.queryset.model

#                 if hasattr(model, "organization") and hasattr(user, "organization"):

#                     field.queryset = field.queryset.filter(
#                         organization=user.organization
#                     )