import logging

from odoo import fields, models

_logger = logging.getLogger(__name__)


class MgmtParagraph(models.Model):
    _inherit = "mgmt.paragraph"

    documentation_ids = fields.One2many(
        "mgmt.documentation",
        "paragraph_id",
    )

    def action_open_paragraph(self):
        return {
            "type": "ir.actions.act_window",
            "res_model": "mgmt.paragraph",
            "res_id": self.id,
            "view_mode": "form",
            "target": "current",
        }
