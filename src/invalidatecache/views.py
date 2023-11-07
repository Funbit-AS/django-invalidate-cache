from django import forms
from django.urls import reverse_lazy
from django.views.generic.edit import FormView
from wagtail.admin import messages
from wagtail.admin.views import generic

from .utils import InvalidateTagError, invalidate_tag


class ManualCacheInvalidationForm(forms.Form):
    tag = forms.CharField(label="Tag", required=True)


class ManualCacheInvalidationView(generic.WagtailAdminTemplateMixin, FormView):
    form_class = ManualCacheInvalidationForm
    template_name = "invalidatecache/admin/form.html"
    success_url = reverse_lazy("manual-cache-invalidation")

    def form_valid(self, form):
        tag = form.cleaned_data["tag"]
        try:
            invalidate_tag(tag)
        except InvalidateTagError:
            messages.error(self.request, f"Error invalidating cache for tag {tag}")
        else:
            messages.success(
                self.request, f"Successfully invalidated cache for tag {tag}"
            )
        return super().form_valid(form)
