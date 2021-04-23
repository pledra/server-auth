# Copyright (C) 2020 GlodoUK <https://www.glodo.uk/>

from odoo import fields, models


class AuthSamlProvider(models.Model):
    _inherit = "auth.saml.provider"

    website_ids = fields.Many2many(
        comodel_name="website",
        relation="auth_saml_provider_website_rel",
        column1="auth_saml_provider_id",
        column2="website_id",
        string="Websites",
        help="A specific list of websites to display this provider upon.",
    )
