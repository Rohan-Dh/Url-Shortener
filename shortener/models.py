from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from .utils import base62_encode

class ShortURL(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name="short_urls")
    original_url = models.URLField()
    code = models.CharField(max_length=20, unique=True, blank=True, db_index=True)

    custom_alias = models.CharField(max_length=30, unique=True, blank=True, null=True)
    expires_at = models.DateTimeField(blank=True, null=True)

    clicks = models.PositiveIntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def is_expired(self):
        return self.expires_at is not None and timezone.now() >= self.expires_at

    def __str__(self):
        return f"{self.code} -> {self.original_url}"
    
    def save(self, *args, **kwargs):
        is_new = self.pk is None
        super().save(*args, **kwargs)
        if is_new and not self.code:
            self.code = base62_encode(self.pk)
            super().save(update_fields=["code"])

