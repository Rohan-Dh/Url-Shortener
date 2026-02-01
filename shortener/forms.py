from django import forms
from django.core.exceptions import ValidationError
from .models import ShortURL
import re

RESERVED = {"create", "edit", "delete", "login", "register", "admin"}

def validate_alias(alias: str, instance_pk=None):
    alias = (alias or "").strip()
    if not alias:
        return None

    if not re.match(r'^[a-zA-Z0-9-]+$', alias):
        raise ValidationError("Alias can contain only letters, numbers, and hyphens.")

    if alias.lower() in RESERVED:
        raise ValidationError("This alias is reserved. Please choose another.")

    qs = ShortURL.objects.filter(code__iexact=alias)
    qs2 = ShortURL.objects.filter(custom_alias__iexact=alias)

    if instance_pk:
        qs = qs.exclude(pk=instance_pk)
        qs2 = qs2.exclude(pk=instance_pk)

    if qs.exists() or qs2.exists():
        raise ValidationError("This alias is already in use.")

    return alias


class ShortURLCreateForm(forms.ModelForm):
    class Meta:
        model = ShortURL
        fields = ["original_url", "custom_alias", "expires_at"]

    def clean_custom_alias(self):
        return validate_alias(self.cleaned_data.get("custom_alias"))


class ShortURLEditForm(forms.ModelForm):
    class Meta:
        model = ShortURL
        fields = ["original_url", "custom_alias", "expires_at"]

    def clean_custom_alias(self):
        return validate_alias(self.cleaned_data.get("custom_alias"), instance_pk=self.instance.pk)
