class AuditUserMixin:
    """
    Automatically assign created_by and updated_by.
    """

    def form_valid(self, form):

        if not form.instance.pk:
            if hasattr(form.instance, "created_by"):
                form.instance.created_by = self.request.user

        if hasattr(form.instance, "updated_by"):
            form.instance.updated_by = self.request.user

        return super().form_valid(form)