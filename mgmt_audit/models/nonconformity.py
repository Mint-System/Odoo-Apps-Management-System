import logging

from odoo import fields, models

_logger = logging.getLogger(__name__)


class MgmtNonconformity(models.Model):
    _name = "mgmt.nonconformity"
    _description = "Mgmt Nonconformity"

    name = fields.Char(required=True)
    type = fields.Selection([
        ('major', 'Major'),
        ('minor', 'Minor'),
    ], required=True)
    task_ids = fields.One2many('project.task')
