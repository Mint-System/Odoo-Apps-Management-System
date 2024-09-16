import logging

from odoo import fields, models

_logger = logging.getLogger(__name__)


class MgmtRiskCombination(models.Model):
    _name = "mgmt.risk.combination"
    _description = "Mgmt Risk Combination"

    name = fields.Char(required=True)
    severity_id = fields.Many2one('mgmt.severity')
    probability_id = fields.Many2one('mgmt.probability', required=True)
