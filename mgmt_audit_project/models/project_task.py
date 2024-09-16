import logging

from odoo import models

_logger = logging.getLogger(__name__)


class ProjectTask(models.Model):
    _inherit = "project.task"

    nonconformity_id = fields.Many2one('mgmt.nonconformity')
    recommendation_id = fields.Many2one('mgmt.recommendation')
