import logging

from odoo import fields, models

_logger = logging.getLogger(__name__)


class MgmtAudit(models.Model):
    _name = "mgmt.audit"
    _description = "Mgmt Audit"

    name = fields.Char()
    type = fields.Selection([  # Type of audit
        ('internal', 'Internal'),
        ('external', 'External'),
        ('extreme', 'Extreme Audits')
    ], required=True)
    plan_end_date = fields.Date()  # Planned end date
    stage_id = fields.Many2one('mgmt.audit.stage')  # Foreign key to audit stage
    responsible_id = fields.Many2one('res.users')  # Responsible user for the audit
    risk_ids = fields.Many2many('mgmt.risk')  # Many2many relationship with risks
    statement_ids = fields.Many2many('mgmt.statement')
