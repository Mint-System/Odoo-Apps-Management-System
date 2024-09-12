import logging

from odoo import fields, models

_logger = logging.getLogger(__name__)


class MgmtHazard(models.Model):
    _inherit = "mgmt.hazard"
