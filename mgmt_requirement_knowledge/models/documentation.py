import logging

from odoo import fields, models

_logger = logging.getLogger(__name__)


class MgmtDocumentation(models.Model):
    _name = "mgmt.documentation"
    _description = "Mgmt Documentation"

    type = fields.Selection(
        [
            ("url", "Url"),
            ("wiki", "Wiki Page"),
        ],
        required=True,
    )
