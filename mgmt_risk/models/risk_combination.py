import logging

from odoo import api, fields, models

_logger = logging.getLogger(__name__)


class MgmtRiskCombination(models.Model):
    _name = "mgmt.risk.combination"
    _description = "Mgmt Risk Combination"

    name = fields.Char(required=True)
    severity_id = fields.Many2one("mgmt.severity")
    probability_id = fields.Many2one("mgmt.probability", required=True)

    @api.model
    def create(self, vals):
        probability = self.env['mgmt.probability'].browse(vals['probability_id'])
        severity = self.env['mgmt.severity'].browse(vals['severity_id'])
        vals['name'] = f"{probability.name} - {severity.name}"
        return super(MgmtRiskCombination, self).create(vals)
