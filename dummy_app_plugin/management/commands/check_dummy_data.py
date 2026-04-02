"""Custom management command to check dummy data for the DummyAppPlugin plugin.

This command is intended to be used for testing as part of CI.
"""

from django.core.management.base import BaseCommand


class Command(BaseCommand):
    """Check dummy data for the DummyAppPlugin plugin."""

    def handle(self, *args, **kwargs):
        """Check dummy data for the DummyAppPlugin plugin."""
        from dummy_app_plugin.models import ExampleModel

        print("Checking dummy data for the DummyAppPlugin plugin")

        keys = [
            "alpha",
            "beta",
            "gamma",
            "delta",
        ]

        for key in keys:
            if not ExampleModel.objects.filter(key=key).exists():
                raise ValueError(f"Example model with key '{key}' does not exist")

        print("- All dummy data for the DummyAppPlugin plugin is present!")
