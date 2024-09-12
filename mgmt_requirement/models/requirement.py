import logging

from odoo import fields, models

_logger = logging.getLogger(__name__)


class MgmtRequirement(models.Model):
    _name = "mgmt.requirement"
    _description = "Mgmt Requirement"

    name = fields.Char()
