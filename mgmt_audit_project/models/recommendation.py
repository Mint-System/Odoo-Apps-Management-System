import logging

from odoo import fields, models

_logger = logging.getLogger(__name__)


class MgmtRecommendation(models.Model):
    _inherit = "mgmt.recommendation"
    _description = "Mgmt Recommendation"

    name = fields.Char(required=True)
    task_ids = fields.One2many("project.task", "recommendation_id")
