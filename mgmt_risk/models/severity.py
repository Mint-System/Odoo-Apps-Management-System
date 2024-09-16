import logging

from odoo import fields, models

_logger = logging.getLogger(__name__)


class MgmtSeverity(models.Model):
    _name = "mgmt.severity"
    _description = "Mgmt Severity"

    name = fields.Char(required=True)
    value = field.Integer(required=True)
