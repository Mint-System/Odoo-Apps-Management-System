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
    display_name = fields.Char(compute="_compute_display_name", store=True)

    @api.depends("name", "reference")
    def _compute_display_name(self):
        for record in self:
            record.display_name = f"{record.name} ({record.reference})"

    def name_get(self):
        result = []
        for paragraph in self:
            name = f"{paragraph.name} ({paragraph.reference})"
            result.append((paragraph.id, name))
        return result
