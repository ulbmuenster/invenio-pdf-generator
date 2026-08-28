# -*- coding: utf-8 -*-
#
# Copyright (C) 2024-2026 University of Münster.
#
# Invenio-Pdf-Generator is free software; you can redistribute it and/or
# modify it under the terms of the MIT License; see LICENSE file for more
# details.

"""Component to hook into the publishing process."""

from flask import current_app
from invenio_drafts_resources.services.records.components import ServiceComponent
from invenio_notifications.models import Notification, Recipient
from invenio_records_resources.proxies import current_service_registry
from invenio_users_resources.proxies import current_users_service

from ..backends.email import EmailWithPdfAttachmentNotificationBackend


class ReceiptComponent(ServiceComponent):
    """Service component for receipt generation."""

    def publish(self, identity, draft=None, record=None, **kwargs):
        """Send a receipt when record is published."""
        users_service = current_users_service
        user = users_service.read(identity, identity.id)
        recipient = Recipient(data=user.data)
        rdm_record_service = current_service_registry.get("records")
        links_item_tpl = rdm_record_service.links_item_tpl
        rdm_record = rdm_record_service.result_item(
            service=rdm_record_service,
            identity=identity,
            record=record,
            links_tpl=links_item_tpl,
            expand=False,
        )
        access = rdm_record.data["parent"]["access"]
        granted_users = []
        further_involved_users = []
        if "grants" in access:
            if "grants" in access:
                for grant in access["grants"]:
                    if grant["subject"]["type"] == "user":
                        granted_user = users_service.read(
                            identity, grant["subject"]["id"]
                        )
                        granted_users.append(granted_user["email"])
                        further_involved_users.append(granted_user.data["profile"])
        context = {
            "request": {
                "receiver": {
                    "access": {
                        "visibility": "restricted",
                    },
                },
                "created_by": user.data,
                "topic": rdm_record,
                "further_involved_users": further_involved_users,
            },
        }
        notification = Notification(type="document-published", context=context)
        email = EmailWithPdfAttachmentNotificationBackend()
        # Further look how o provide the locale -> should first run in the UI
        current_app.logger.info("Send mail now!")
        email.send(notification=notification, recipient=recipient, cc=granted_users)
