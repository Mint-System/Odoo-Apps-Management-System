import logging

from odoo import fields, models

_logger = logging.getLogger(__name__)


class MgmtHazard(models.Model):
    _inherit = "mgmt.hazard"

    severity_id = fields.Many2one('mgmt.severity')
    probability_id = fields.Many2one('mgmt.probability')
