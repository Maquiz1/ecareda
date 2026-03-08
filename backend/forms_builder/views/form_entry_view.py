from django.views import View
from django.shortcuts import render, redirect, get_object_or_404
from forms_builder.models import FormResponse, FieldValue
from django.utils import timezone


class FormEntryView(View):

    template_name = "forms_builder/form_entry.html"

    def get(self, request, pk):
        form_response = get_object_or_404(FormResponse, pk=pk)

        # fields = form_response.form.field_values.all()
        fields = form_response.form.formfielddefinition_set.all()

        existing_values = {
            fv.field_id: fv.value
            for fv in FieldValue.objects.filter(form_response=form_response)
            # for fv in FieldValue.objects.filter(response=form_response)
        }

        return render(request, self.template_name, {
            "form_response": form_response,
            "fields": fields,
            "values": existing_values
        })

    def post(self, request, pk):
        form_response = get_object_or_404(FormResponse, pk=pk)

        if form_response.status == "locked":
            return redirect("visit_detail", pk=form_response.visit.pk)

        fields = form_response.form.field_values.all()
        # fields = form_response.form.formfielddefinition_set.all()

        for field in fields:
            value = request.POST.get(str(field.id))

            FieldValue.objects.update_or_create(
                form_response=form_response,
                field=field,
                defaults={"value": value}
            )

        form_response.status = "completed"
        form_response.save()

        return redirect("visit_detail", pk=form_response.visit.pk)