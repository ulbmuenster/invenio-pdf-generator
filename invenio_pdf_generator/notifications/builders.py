# -*- coding: utf-8 -*-
#
# Copyright (C) 2023-2026 University of Münster.
#
# Invenio-Pdf-Generator is free software; you can redistribute it and/or
# modify it under the terms of the MIT License; see LICENSE file for more
# details.

"""Notification related utils for notifications."""

from invenio_rdm_records.notifications.builders import (
    CommunityInclusionAcceptNotificationBuilder,
    CommunityInclusionSubmittedNotificationBuilder,
)
from invenio_users_resources.notifications.filters import UserPreferencesRecipientFilter

from invenio_pdf_generator.notifications.filters import SuppressingNotificationFilter
from invenio_pdf_generator.services.generators import UserEmailWithPdfAttachmentBackend


class CommunityInclusionSubmittedNGNotificationBuilder(
    CommunityInclusionSubmittedNotificationBuilder
):
    """Submission notification can include a PDF attachment."""

    recipient_filters = [
        UserPreferencesRecipientFilter(),
    ]

    recipient_backends = [
        UserEmailWithPdfAttachmentBackend(),
    ]


class CommunityInclusionAcceptNGNotificationBuilder(
    CommunityInclusionAcceptNotificationBuilder
):
    """Accept notification can include a PDF attachment."""

    recipient_filters = [
        SuppressingNotificationFilter(),
    ]

    recipient_backends = [
        UserEmailWithPdfAttachmentBackend(),
    ]
