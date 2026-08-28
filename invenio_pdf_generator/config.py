# -*- coding: utf-8 -*-
#
# Copyright (C) 2023-2026 University of Münster.
#
# Invenio-Pdf-Generator is free software; you can redistribute it and/or
# modify it under the terms of the MIT License; see LICENSE file for more
# details.

"""Invenio module that generates PDF from jinja2 templates."""

PDF_GENERATOR_DEFAULT_VALUE = "foobar"
"""Default value for the application."""

PDF_GENERATOR_BASE_TEMPLATE = "invenio_pdf_generator/base.html"
"""Default base template for the demo page."""

PDF_GENERATOR_NAME_PREFIX = "certificate_"
"""Default prefix of the pdf certificate filename."""

"""
from invenio_app_rdm.config import (
    NOTIFICATIONS_BACKENDS,
    NOTIFICATIONS_BUILDERS,
)
from invenio_pdf_generator.backends import EmailWithPdfAttachmentNotificationBackend
from invenio_pdf_generator.notifications.builders import (
    CommunityInclusionAcceptNGNotificationBuilder,
    CommunityInclusionSubmittedNGNotificationBuilder,
)
from invenio_rdm_records.notifications.builders import (
    CommunityInclusionAcceptNotificationBuilder,
    CommunityInclusionSubmittedNotificationBuilder,
)

NOTIFICATIONS_BACKENDS = {
  **NOTIFICATIONS_BACKENDS,
  EmailWithPdfAttachmentNotificationBackend.id: EmailWithPdfAttachmentNotificationBackend(),
}

NOTIFICATIONS_BUILDERS = {
  **NOTIFICATIONS_BUILDERS,
  CommunityInclusionAcceptNotificationBuilder.type: CommunityInclusionAcceptNGNotificationBuilder,
  CommunityInclusionSubmittedNotificationBuilder.type: CommunityInclusionSubmittedNGNotificationBuilder,
}
"""
