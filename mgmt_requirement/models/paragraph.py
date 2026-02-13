import logging

from odoo import api, fields, models

_logger = logging.getLogger(__name__)


class MgmtParagraph(models.Model):
    _name = "mgmt.paragraph"
    _description = "Mgmt Paragraph"

    name = fields.Char(required=True)
    description = fields.Html()
    reference = fields.Char(required=True)
    document_id = fields.Many2one("mgmt.document")
    tag_ids = fields.Many2many("mgmt.requirement.tag")

    display_name = fields.Char(
        compute="_compute_display_name",
        store=True,
    )

    @api.depends("name", "reference", "document_id.name")
    def _compute_display_name(self):
        for rec in self:
            parts = []
            if rec.document_id:
                parts.append(f"{rec.document_id.name}")
            if rec.reference:
                parts.append(f"{rec.reference}")
            if rec.name:
                parts.append(rec.name)

            if len(parts) > 1:
                rec.display_name = " - ".join(parts)
            else:
                rec.display_name = "".join(parts)
