import logging

from odoo import fields, models

_logger = logging.getLogger(__name__)


class MgmtAudit(models.Model):
    _name = "mgmt.audit"
    _description = "Mgmt Audit"

    name = fields.Char(required=True)
    requirement_ids = fields.Many2many('mgmt.requirement')
    type = fields.Selection([
        ('internal', 'Internal'),
        ('external', 'External'),
    ])
    planned_date = fields.Date()
    stage_id = fields.Many2one('mgmt.audit.stage')
    responsible_id = fields.Many2one('hr.employee')
    statement_ids = fields.Many2many('mgmt.statement')
    auditor_ids = fields.Many2many('res.partner')
