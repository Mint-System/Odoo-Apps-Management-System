import logging

from odoo import models

_logger = logging.getLogger(__name__)


class ProjectTask(models.Model):
    _inherit = "project.task"
