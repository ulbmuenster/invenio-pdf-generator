..
    Copyright (C) 2023-2026 University of Münster.

    Invenio-Pdf-Generator is free software; you can redistribute it and/or
    modify it under the terms of the MIT License; see LICENSE file for more
    details.

=======================
 Invenio-Pdf-Generator
=======================

Invenio Module, generating PDF files and mail texts (plain and html) from Jinja2 Templates and sending them by mail.
It offers two possible ways of processing: either as component hooking into the publishing pipeline or hooking into the notification pipeline of community inclusion.

The component based setup decides who is receiving the mail based on the available grants.

Configuration of Component-based way
------------------------------------


    # --------------------------------------------------------

    # PDF Receipt

    # --------------------------------------------------------

    from invenio_pdf_generator.components import ReceiptComponent
    
    from invenio_rdm_records.services.components import DefaultRecordsComponents

    RDM_RECORDS_SERVICE_COMPONENTS = DefaultRecordsComponents + [..., ReceiptComponent]


Configuration of Community-based way
------------------------------------


    # Settings for invenio-pdf-generator

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


Authors
-------

- University of Münster <forschungsdaten@uni-muenster.de>

Disclaimer
----------

This project is not an official Invenio module. It is neither maintained by nor
affiliated with CERN or the Invenio collaboration.

The software is provided "as is", without warranty of any kind, express or
implied, including but not limited to the warranties of merchantability,
fitness for a particular purpose and noninfringement. In no event shall the
authors or copyright holders be liable for any claim, damages or other
liability, whether in an action of contract, tort or otherwise, arising from,
out of or in connection with the software or the use or other dealings in the
software.
