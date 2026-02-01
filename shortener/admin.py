from django.contrib import admin
from .models import ShortURL

@admin.register(ShortURL)
class ShortURLAdmin(admin.ModelAdmin):
    list_display = ("code", "owner", "original_url", "clicks", "created_at", "expires_at")
    search_fields = ("code", "original_url", "owner__username")
    list_filter = ("created_at",)
