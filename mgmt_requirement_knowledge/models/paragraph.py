import logging

from odoo import api, fields, models

_logger = logging.getLogger(__name__)


class MgmtParagraph(models.Model):
    _inherit = "mgmt.paragraph"

    documentation_ids = fields.Many2many(
        "mgmt.documentation",
        "mgmt_paragraph_documentation_rel",
        "paragraph_id",
        "documentation_id",
        string="Documentations",
    )

    def action_open_paragraph(self):
        return {
            "type": "ir.actions.act_window",
            "res_model": "mgmt.paragraph",
            "res_id": self.id,
            "view_mode": "form",
            "target": "current",
        }
