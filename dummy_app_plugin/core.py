"""An InvenTree plugin which provides custom data tables"""

from plugin import InvenTreePlugin

from plugin.mixins import AppMixin, SettingsMixin

from . import PLUGIN_VERSION


class DummyAppPlugin(AppMixin, SettingsMixin, InvenTreePlugin):
    """DummyAppPlugin - custom InvenTree plugin."""

    # Plugin metadata
    TITLE = "Dummy App Plugin"
    NAME = "DummyAppPlugin"
    SLUG = "dummy-app-plugin"
    DESCRIPTION = "An InvenTree plugin which provides custom data tables"
    VERSION = PLUGIN_VERSION

    # Additional project information
    AUTHOR = "Oliver Walters"
    WEBSITE = "https://github.com/inventree/dummy-plugin"
    LICENSE = "MIT"

    MIN_VERSION = "1.2.0"

    # Plugin settings (from SettingsMixin)
    SETTINGS = {
        # Define your plugin settings here...
        "CUSTOM_VALUE": {
            "name": "Custom Value",
            "description": "A custom value",
            "validator": int,
            "default": 42,
        }
    }
