import logging

from odoo import api, fields, models

_logger = logging.getLogger(__name__)


class MgmtSeverity(models.Model):
    _name = "mgmt.severity"
    _description = "Mgmt Severity"

    name = fields.Char(required=True)
    value = fields.Integer(required=True)

    @api.model
    def create(self, vals):
        severity = super(MgmtSeverity, self).create(vals)
        probabilities = self.env['mgmt.probability'].search([])

        for probability in probabilities:
            self.env['mgmt.risk.combination'].create({
                'name': f"{probability.name} - {severity.name}",
                'probability_id': probability.id,
                'severity_id': severity.id,
            })
        return severity

    def unlink(self):
        combinations = self.env['mgmt.risk.combination'].search([('severity_id', 'in', self.ids)])
        combinations.unlink()
        return super(MgmtSeverity, self).unlink()
