import logging

from odoo import fields, models

_logger = logging.getLogger(__name__)


class MgmtRisk(models.Model):
    _name = "mgmt.risk"
    _description = "Mgmt Risk"

    name = fields.Char()
