import logging

from odoo import fields, models

_logger = logging.getLogger(__name__)


class MgmtNonconformity(models.Model):
    _name = "mgmt.nonconformity"
    _description = "Mgmt Nonconformity"

    name = fields.Char()
