import logging

from odoo import fields, models

_logger = logging.getLogger(__name__)


class MgmtParagraph(models.Model):
    _name = "mgmt.paragraph"
    _description = "Mgmt Paragraph"

    name = fields.Char(required=True)
    description = fields.Html()
    reference = fields.Char(required=True)
    document_id = fields.Many2one("mgmt.document")
    tag_ids = fields.Many2many("mgmt.requirement.tag")

    def name_get(self):
        result = []
        for paragraph in self:
            name = f"{paragraph.name} ({paragraph.reference})"
            result.append((paragraph.id, name))
        return result
