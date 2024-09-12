import logging

from odoo import fields, models

_logger = logging.getLogger(__name__)


class MgmtStatement(models.Model):
    _name = "mgmt.statement"
    _description = "Mgmt Statement"

    name = fields.Char()
