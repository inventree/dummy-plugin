"""Custom model definitions for the DummyAppPlugin plugin.

This file is where you can define any custom database models.

- Any models defined here will require database migrations to be created.
- Don't forget to register your models in the admin interface if needed!
"""

from django.db import models
from django.utils.translation import gettext_lazy as _


class ExampleModel(models.Model):
    """An example model for the DummyAppPlugin plugin."""

    class Meta:
        """Meta options for the model."""

        app_label = "dummy_app_plugin"
        verbose_name = _("Example Model")
        verbose_name_plural = _("Example Models")

    key = models.CharField(
        max_length=100,
        unique=True,
        verbose_name=_("Key"),
        help_text=_("A unique key for the example model"),
    )

    value = models.CharField(
        max_length=255,
        verbose_name=_("Value"),
        help_text=_("A value associated with the key"),
    )
