import logging

from odoo import fields, models

_logger = logging.getLogger(__name__)


class MgmtRisk(models.Model):
    _inherit = "mgmt.risk"

    asset_ids = fields.Many2many("mgmt.asset", required=True)
