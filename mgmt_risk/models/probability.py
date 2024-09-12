import logging

from odoo import fields, models

_logger = logging.getLogger(__name__)


class MgmtProbability(models.Model):
    _name = "mgmt.probability"
    _description = "Mgmt Probability"

    name = fields.Char()
