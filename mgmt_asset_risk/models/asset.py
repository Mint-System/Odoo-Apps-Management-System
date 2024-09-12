import logging

from odoo import fields, models

_logger = logging.getLogger(__name__)


class MgmtAsset(models.Model):
    _inherit = "mgmt.asset"

