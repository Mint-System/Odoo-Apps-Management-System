import logging

from odoo import api, fields, models

_logger = logging.getLogger(__name__)


class MgmtProbability(models.Model):
    _name = "mgmt.probability"
    _description = "Mgmt Probability"

    name = fields.Char(required=True)
    value = fields.Integer(required=True)

    @api.model
    def create(self, vals):
        probability = super(MgmtProbability, self).create(vals)
        severities = self.env['mgmt.severity'].search([])

        for severity in severities:
            self.env['mgmt.risk.combination'].create({
                'probability_id': probability.id,
                'severity_id': severity.id,
            })
        return probability

    def unlink(self):
        combinations = self.env['mgmt.risk.combination'].search([('probability_id', 'in', self.ids)])
        combinations.unlink()
        return super(MgmtProbability, self).unlink()
