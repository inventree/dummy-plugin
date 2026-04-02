"""Django config for the DummyAppPlugin plugin."""

from django.apps import AppConfig


class DummyAppPluginConfig(AppConfig):
    """Config class for the DummyAppPlugin plugin."""

    name = "dummy_app_plugin"

    def ready(self):
        """This function is called whenever the DummyAppPlugin plugin is loaded."""
        ...
