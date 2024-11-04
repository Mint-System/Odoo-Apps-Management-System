import logging

from odoo import fields, models

_logger = logging.getLogger(__name__)


class MgmtRecommendation(models.Model):
    _name = "mgmt.recommendation"
    _description = "Mgmt Recommendation"
    _inherit = ['mail.thread', 'mail.activity.mixin']

    name = fields.Char(required=True)
