import logging

from odoo import fields, models

_logger = logging.getLogger(__name__)


class MgmtRecommendation(models.Model):
    _name = "mgmt.recommendation"
    _description = "Mgmt Recommendation"

    name = fields.Char()
    task_ids = fields.One2many('project.task')
