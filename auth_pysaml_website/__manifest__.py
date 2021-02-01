# Copyright (C) 2020 GlodoUK <https://www.glodo.uk/>
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

{
    "name": "Saml2 Authentication Integration with Website",
    "version": "14.0.1.0.0",
    "category": "Tools",
    "author": "Odoo Community Association (OCA)",
    "website": "https://github.com/OCA/server-auth",
    "license": "AGPL-3",
    "depends": ["auth_pysaml"],
    "external_dependencies": {"python": []},
    "demo": [],
    "data": [
        "views/auth_saml.xml",
    ],
    "installable": True,
    "auto_install": False,
    "summary": """
    Allows saml provider buttons to be filtered by website
    """,
}
