"""Admin site configuration for the DummyAppPlugin plugin."""

from django.contrib import admin

from .models import ExampleModel


@admin.register(ExampleModel)
class ExampleModelAdmin(admin.ModelAdmin):
    """Admin interface for the ExampleModel."""

    list_display = ("key", "value")
