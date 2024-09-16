import logging

from odoo import fields, models

_logger = logging.getLogger(__name__)

class ResCompany(models.Model):
    _inherit = 'res.company'

    mgmt_audit_project_id = fields.Many2one('project.project')

class ResConfigSettings(models.Model):
    _inherit = "res.config.settings"

    mgmt_audit_project_id = fields.Many2one(
        related='company_id.mgmt_audit_project_id',
        readonly=False
    )
