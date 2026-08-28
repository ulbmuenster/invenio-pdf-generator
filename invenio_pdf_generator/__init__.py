# -*- coding: utf-8 -*-
#
# Copyright (C) 2023-2026 University of Münster.
#
# Invenio-Pdf-Generator is free software; you can redistribute it and/or
# modify it under the terms of the MIT License; see LICENSE file for more
# details.

"""Invenio module that generates PDF from jinja2 templates."""

from .ext import InvenioPdfGenerator

__version__ = "0.9.1"

__all__ = ("__version__", "InvenioPdfGenerator")
