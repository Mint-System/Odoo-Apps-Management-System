import logging

from odoo import fields, models

_logger = logging.getLogger(__name__)


class MgmtRequirement(models.Model):
    _name = "mgmt.requirement"
    _description = "Mgmt Requirement"

    name = fields.Char(required=True)
    description = fields.Text()
    system_id = fields.Many2one('mgmtsystem.system')
    paragraph_ids = fields.Many2many('mgmt.paragraph')
    #statement_ids = fields.One2many('mgmt.statement', 'requirement_id')
