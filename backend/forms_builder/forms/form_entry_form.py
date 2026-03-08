from django import forms
from forms_builder.models import FormFieldDefinition
from core.forms.bootstrap_mixin import BootstrapTenantMixin


class DynamicFormEntry(BootstrapTenantMixin, forms.Form):

    def __init__(self, *args, form=None, values=None, request=None, **kwargs):

        self.request = request
        super().__init__(*args, **kwargs)

        fields = FormFieldDefinition.objects.filter(
            form=form
        ).order_by("order")

        for field in fields:

            field_name = f"field_{field.id}"

            initial = None
            if values:
                initial = values.get(str(field.id))

            form_field = self.create_form_field(field, initial)

            self.fields[field_name] = form_field

        self.apply_tenant_and_style()


    def parse_choices(self, choices_string):

        choices = []

        for item in choices_string.split(","):

            item = item.strip()

            if "=" in item:
                value, label = item.split("=", 1)
                choices.append((value.strip(), label.strip()))
            else:
                choices.append((item, item))

        return choices

    def create_form_field(self, field, initial):

        if field.field_type == "text":

            return forms.CharField(
                label=field.label,
                required=field.required,
                initial=initial
            )


        elif field.field_type == "number":

            return forms.IntegerField(
                label=field.label,
                required=field.required,
                initial=initial
            )


        elif field.field_type == "date":

            return forms.DateField(
                label=field.label,
                required=field.required,
                initial=initial,
                widget=forms.DateInput(attrs={"type": "date"})
            )


        elif field.field_type == "select":

            choices = []

            if field.choices:
                choices = self.parse_choices(field.choices) if field.choices else []

            return forms.ChoiceField(
                label=field.label,
                required=field.required,
                choices=[("", "---------")] + choices,
                initial=initial
            )


        elif field.field_type == "checkbox":

            # multiple checkbox options
            if field.choices:

                choices = self.parse_choices(field.choices)

                return forms.MultipleChoiceField(
                    label=field.label,
                    required=False,
                    choices=choices,
                    initial=initial,
                    widget=forms.CheckboxSelectMultiple
                )

            # single checkbox
            return forms.BooleanField(
                label=field.label,
                required=False,
                initial=initial
            )
            
        elif field.field_type == "radio":

            choices = []

            if field.choices:
                choices = self.parse_choices(field.choices) if field.choices else []

            return forms.ChoiceField(
                label=field.label,
                required=field.required,
                choices=choices,
                initial=initial,
                widget=forms.RadioSelect
            )
            
        elif field.field_type == "textarea":

            return forms.CharField(
                label=field.label,
                required=field.required,
                initial=initial,
                widget=forms.Textarea(attrs={"rows":4})
            )


        return forms.ChoiceField(
            label=field.label,
            required=field.required,
            initial=initial,
        )