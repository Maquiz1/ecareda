from django import forms
from forms_builder.models import FormFieldDefinition
from core.forms.bootstrap_mixin import BootstrapTenantMixin


class DynamicFormEntry(BootstrapTenantMixin, forms.Form):

    def __init__(self, *args, form=None, values=None, request=None, **kwargs):

        self.request = request

        super().__init__(*args, **kwargs)

        fields = FormFieldDefinition.objects.filter(
            form=form,
            # is_deleted=False
        ).order_by("order")

        for field in fields:

            initial = None
            if values:
                initial = values.get(str(field.id))

            self.fields[str(field.id)] = forms.CharField(
                label=field.label,
                required=field.required,
                initial=initial
            )

        # Apply tenant filtering + styling
        self.apply_tenant_and_style()