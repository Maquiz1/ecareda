from django import forms


class TenantModelForm(forms.ModelForm):
    """
    Restricts queryset fields to the user's organization.
    """

    def __init__(self, *args, **kwargs):

        self.request = kwargs.pop("request", None)

        super().__init__(*args, **kwargs)

        if not self.request:
            return

        user = self.request.user

        for field in self.fields.values():

            if hasattr(field, "queryset"):

                model = field.queryset.model

                if hasattr(model, "organization") and hasattr(user, "organization"):

                    field.queryset = field.queryset.filter(
                        organization=user.organization
                    )