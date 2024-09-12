import logging

from odoo import fields, models

_logger = logging.getLogger(__name__)


class MgmtRisk(models.Model):
    _name = "mgmt.risk"
    _description = "Mgmt Risk"

    name = fields.Char()

class MgmtRiskCombination(models.Model):
    _name = "mgmt.risk.combination"
    _description = "Mgmt Risk Combination"

    name = fields.Char()