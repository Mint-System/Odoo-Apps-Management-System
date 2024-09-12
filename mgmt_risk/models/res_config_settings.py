import logging

from odoo import fields, models

_logger = logging.getLogger(__name__)


class ResConfigSettings(models.TransientModel):
    _inherit = "res.config.settings"

    mgmt_risk_formula = fields.Selection(
        [
            ("multiply", "A*B"),
            ("sum", "A+B"),
        ]
    )
