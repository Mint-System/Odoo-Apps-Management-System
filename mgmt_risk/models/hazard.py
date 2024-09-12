import logging

from odoo import fields, models

_logger = logging.getLogger(__name__)


class MgmtHazard(models.Model):
    _name = "mgmt.hazard"
    _description = "Mgmt Hazard"

    name = fields.Char()
