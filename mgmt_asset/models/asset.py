import logging

from odoo import fields, models

_logger = logging.getLogger(__name__)


class MgmtAsset(models.Model):
    _name = "mgmt.asset"
    _description = "Mgmt Asset"

    name = fields.Char()
