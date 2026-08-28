# -*- coding: utf-8 -*-
#
# Copyright (C) 2023-2026 University of Münster.
#
# Invenio-Pdf-Generator is free software; you can redistribute it and/or
# modify it under the terms of the MIT License; see LICENSE file for more
# details.

"""Generators for notification context."""

from invenio_notifications.services.generators import RecipientBackendGenerator

from invenio_pdf_generator.backends.email import (
    EmailWithPdfAttachmentNotificationBackend,
)


class UserEmailWithPdfAttachmentBackend(RecipientBackendGenerator):
    """User related email backend generator for a notification."""

    def __call__(self, notification, recipient, backends):
        """Add backend id to backends."""
        backend_id = EmailWithPdfAttachmentNotificationBackend.id
        backends.append(backend_id)
        return backend_id
