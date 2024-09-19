import logging

from odoo import api, fields, models

_logger = logging.getLogger(__name__)


class MgmtRiskCombination(models.Model):
    _name = "mgmt.risk.combination"
    _description = "Mgmt Risk Combination"
    _order = "name"

    name = fields.Char(required=True)
    severity_id = fields.Many2one("mgmt.severity", readonly=True, required=True)
    probability_id = fields.Many2one("mgmt.probability", readonly=True, required=True)
