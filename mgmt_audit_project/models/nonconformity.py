import logging

from odoo import models

_logger = logging.getLogger(__name__)


class MgmtNonconformity(models.Model):
    _inherit = "mgmt.nonconformity"
