"""Custom management command to generate date for the DummyAppPlugin plugin.

This command is intended to be used for testing as part of CI.
"""

from django.core.management.base import BaseCommand


class Command(BaseCommand):
    """Generate dummy data for the DummyAppPlugin plugin."""

    def handle(self, *args, **kwargs):
        """Generate dummy data for the DummyAppPlugin plugin."""
        from dummy_app_plugin.models import ExampleModel

        print("Generating dummy data for the DummyAppPlugin plugin")

        keys = [
            "alpha",
            "beta",
            "gamma",
            "delta",
        ]

        for key in keys:
            if ExampleModel.objects.filter(key=key).exists():
                print(f"- Example model with key '{key}' already exists")
            else:
                print(f"- Creating example model with key '{key}'")
                ExampleModel.objects.create(
                    key=key,
                    value=f"Value for {key}",
                )
