# -*- coding: utf-8 -*-
#
# Copyright (C) 2023-2026 University of Münster.
#
# Invenio-Pdf-Generator is free software; you can redistribute it and/or
# modify it under the terms of the MIT License; see LICENSE file for more
# details.

"""E-mail with pdf-attachment specific notification backend."""

from base64 import b64encode
from datetime import datetime

from flask import current_app
from invenio_mail.tasks import send_email_with_attachments
from invenio_notifications.backends.base import NotificationBackend
from marshmallow_utils.html import strip_html

from invenio_pdf_generator.backends.utils import JinjaPdfTemplateLoaderMixin


class EmailWithPdfAttachmentNotificationBackend(
    NotificationBackend, JinjaPdfTemplateLoaderMixin
):
    """E-mail with pdf-attachment specific notification backend."""

    id = "email_with_pdf"

    def send(self, notification, recipient, cc=None):
        """Mail sending implementation."""
        content = self.render_template(notification, recipient)
        pdf_content = self.render_pdf_template(notification, recipient)

        message = {
            "subject": content["subject"],
            "html": content["html_body"],
            "body": strip_html(content["plain_body"]),
            "recipients": [
                recipient.data.get("email") or recipient.data.get("email_hidden")
            ],
            "sender": current_app.config["MAIL_DEFAULT_SENDER"],
            "reply_to": current_app.config["MAIL_DEFAULT_REPLY_TO"],
        }
        if cc:
            message["cc"] = cc
        filename_prefix = current_app.config["PDF_GENERATOR_NAME_PREFIX"]
        today = datetime.now().strftime("%Y-%m-%d")
        resp = send_email_with_attachments(
            message,
            [
                {
                    "base64": b64encode(pdf_content),
                    "content_type": "application/pdf",
                    "disposition": "attachment",
                    "filename": filename_prefix + today + ".pdf",
                }
            ],
        )
        return resp
