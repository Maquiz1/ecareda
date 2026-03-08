from django import forms


class BootstrapTenantMixin:
    """
    Reusable mixin for:
    - Tenant filtering
    - Bootstrap styling
    - Date picker support
    """

    def apply_tenant_and_style(self):

        user = getattr(self.request, "user", None)

        for name, field in self.fields.items():

            # -----------------------------
            # Tenant filtering
            # -----------------------------
            if hasattr(field, "queryset") and user:

                model = field.queryset.model

                if hasattr(model, "organization") and hasattr(user, "organization"):

                    field.queryset = field.queryset.filter(
                        organization=user.organization
                    )

            # -----------------------------
            # Bootstrap styling
            # -----------------------------
            if isinstance(field.widget, forms.CheckboxInput):

                field.widget.attrs["class"] = "form-check-input"

            elif isinstance(field.widget, forms.Select):

                field.widget.attrs["class"] = "form-select"

            else:

                field.widget.attrs["class"] = "form-control"
                field.widget.attrs["placeholder"] = field.label

            # -----------------------------
            # Date picker
            # -----------------------------
            if isinstance(field, forms.DateField):

                field.widget = forms.DateInput(
                    attrs={
                        "type": "date",
                        "class": "form-control"
                    }
                )