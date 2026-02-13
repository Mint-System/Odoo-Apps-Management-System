import logging

from odoo import fields, models

_logger = logging.getLogger(__name__)


class MgmtRequirement(models.Model):
    _inherit = "mgmt.requirement"

    statement_ids = fields.One2many("mgmt.statement", "requirement_id")
