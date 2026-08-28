# -*- coding: utf-8 -*-
#
# Copyright (C) 2023-2026 University of Münster.
#
# Invenio-Pdf-Generator is free software; you can redistribute it and/or
# modify it under the terms of the MIT License; see LICENSE file for more
# details.

"""Invenio module that generates PDF from jinja2 templates."""

from flask_babel import gettext as _

from . import config


class InvenioPdfGenerator(object):
    """Invenio-Pdf-Generator extension."""

    def __init__(self, app=None):
        """Extension initialization."""
        if app:
            self.init_app(app)

    def init_app(self, app):
        """Flask application initialization."""
        self.init_config(app)
        app.extensions["invenio-pdf-generator"] = self

    def init_config(self, app):
        """Initialize configuration."""
        # Use theme's base template if theme is installed
        if "BASE_TEMPLATE" in app.config:
            app.config.setdefault(
                "PDF_GENERATOR_BASE_TEMPLATE",
                app.config["BASE_TEMPLATE"],
            )
        for k in dir(config):
            if k.startswith("PDF_GENERATOR_"):
                app.config.setdefault(k, getattr(config, k))
