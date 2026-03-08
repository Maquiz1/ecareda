from django.views import View
from django.shortcuts import render, redirect, get_object_or_404

from forms_builder.models import FormResponse, FieldValue
from ..forms import DynamicFormEntry


class FormEntryView(View):

    template_name = "forms_builder/form_entry.html"

    def get(self, request, pk):

        form_response = get_object_or_404(FormResponse, pk=pk)

        existing_values = {
            str(fv.field_id): fv.value
            for fv in FieldValue.objects.filter(form_response=form_response)
        }

        form = DynamicFormEntry(
            form=form_response.form,
            values=existing_values,
            request=request
        )

        return render(request, self.template_name, {
            "form_response": form_response,
            "form": form
        })


    def post(self, request, pk):

        form_response = get_object_or_404(FormResponse, pk=pk)

        if form_response.status == "locked":
            return redirect("visits:visit_detail", pk=form_response.visit.pk)

        form = DynamicFormEntry(
            request.POST,
            form=form_response.form,
            request=request
        )

        if form.is_valid():

            for field_id, value in form.cleaned_data.items():

                FieldValue.objects.update_or_create(
                    form_response=form_response,
                    field_id=field_id,
                    defaults={"value": value}
                )

            form_response.status = "completed"
            form_response.save()

            return redirect("visits:visit_detail", pk=form_response.visit.pk)

        return render(request, self.template_name, {
            "form_response": form_response,
            "form": form
        })