import logging

from odoo import fields, models

_logger = logging.getLogger(__name__)


class MgmtRisk(models.Model):
    _name = "mgmt.risk"
    _description = "Mgmt Risk"

    name = fields.Char()
    description = fields.Text()

    risk_owner_id = fields.Many2one('res.users', required=True)
    asset_ids = fields.Many2many('mgmt.asset', required=True)
    severity_id = fields.Many2one('mgmt.severity', required=True)
    hazard_ids = fields.Many2many('mgmt.hazard', required=True)
    revision_risk_ids = fields.One2many('mgmt.risk', 'head_risk_id')
    head_risk_id = fields.Many2one('mgmt.risk')
    probability_id = fields.Many2one('mgmt.probability', required=True)
    risk_score = fields.Float(compute='_compute_risk_score', store=True)
    color = fields.Integer(compute='_compute_color', store=True)
    stage = fields.Selection([
        ('identify', 'Identify'),
        ('evaluate_threat', 'Evaluate Threat'),
        ('monitor', 'Monitor')
    ], required=True)
