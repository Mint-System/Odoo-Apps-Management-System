import logging

from odoo import fields, models

_logger = logging.getLogger(__name__)


class MgmtAuditStage(models.Model):
    _name = "mgmt.audit.stage"
    _description = "Mgmt Audit Stage"

    name = fields.Char(required=True)
    code = fields.Char(required=True)
    sequence = fields.Char(required=True)
