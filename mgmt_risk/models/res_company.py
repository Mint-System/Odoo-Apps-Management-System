import logging

from odoo import fields, models

_logger = logging.getLogger(__name__)


class ResCompany(models.Model):
    _inherit = "res.company"

    mgmt_risk_formula = fields.Selection(
        [
            ("multiply", "Severity * Probability"),
            ("sum", "Severity + Probability")
        ]
    )

class ResConfigSettings(models.TransientModel):
    _inherit = "res.config.settings"

    mgmt_risk_formula = fields.Selection(
        related='company_id.mgmt_risk_formula',
        readonly=False
    )
