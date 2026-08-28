# -*- coding: utf-8 -*-
#
# Copyright (C) 2023-2026 University of Münster.
#
# Invenio-Pdf-Generator is free software; you can redistribute it and/or
# modify it under the terms of the MIT License; see LICENSE file for more
# details.

"""Module tests."""

from flask import Flask

from invenio_pdf_generator import InvenioPdfGenerator


def test_version():
    """Test version import."""
    from invenio_pdf_generator import __version__

    assert __version__


def test_init():
    """Test extension initialization."""
    app = Flask("testapp")
    ext = InvenioPdfGenerator(app)
    assert "invenio-pdf-generator" in app.extensions

    app = Flask("testapp")
    ext = InvenioPdfGenerator()
    assert "invenio-pdf-generator" not in app.extensions
    ext.init_app(app)
    assert "invenio-pdf-generator" in app.extensions
