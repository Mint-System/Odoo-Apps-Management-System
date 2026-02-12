import logging

from odoo import fields, models

_logger = logging.getLogger(__name__)


class MgmtRiskStage(models.Model):
    _name = "mgmt.risk.stage"
    _description = "Mgmt Risk Stage"

    name = fields.Char(required=True)
    code = fields.Char(required=True)
    sequence = fields.Char(required=True)
