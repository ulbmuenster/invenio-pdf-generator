# -*- coding: utf-8 -*-
#
# Copyright (C) 2023-2026 University of Münster.
#
# Invenio-Pdf-Generator is free software; you can redistribute it and/or
# modify it under the terms of the MIT License; see LICENSE file for more
# details.

"""Filter that suppresses all notifications."""

from invenio_notifications.services.filters import RecipientFilter


class SuppressingNotificationFilter(RecipientFilter):
    """Filter that suppresses all notifications."""

    def __call__(self, notification, recipients):
        """Filter everybody."""
        for key in list(recipients.keys()):
            del recipients[key]

        return recipients
