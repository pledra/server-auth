# Copyright (C) 2020 GlodoUK <https://www.glodo.uk/>

from odoo.http import request
from odoo.osv import expression

from odoo.addons.web.controllers.main import Home


class SAMLLogin(Home):
    def _list_saml_providers_domain(self):
        domain = super()._list_saml_providers_domain()

        website_id = getattr(request, "website", None)
        if website_id:
            domain = expression.AND(
                [
                    domain,
                    [
                        "|",
                        ("website_ids", "=", website_id.id),
                        ("website_ids", "=", False),
                    ],
                ]
            )

        return domain
