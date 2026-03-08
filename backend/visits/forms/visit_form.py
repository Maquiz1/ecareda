# visits/forms.py

from core.forms.tenant_model_form import TenantModelForm
from visits.models import Visit


class VisitForm(TenantModelForm):

    class Meta:
        model = Visit
        fields = [
            "visit_type",
            "visit_number",
            "visit_date",
            "notes",
        ]