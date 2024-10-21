import logging

from odoo import fields, models

_logger = logging.getLogger(__name__)


class MgmtRequirement(models.Model):
    _name = "mgmt.requirement"
    _description = "Mgmt Requirement"

    name = fields.Char(required=True)
    description = fields.Html()
    system_id = fields.Many2one("mgmt.system")
    paragraph_ids = fields.Many2many("mgmt.paragraph")
