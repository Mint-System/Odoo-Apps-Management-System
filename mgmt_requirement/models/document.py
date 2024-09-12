import logging

from odoo import fields, models

_logger = logging.getLogger(__name__)


class MgmtDocument(models.Model):
    _name = "mgmt.document"
    _description = "Mgmt Document"

    name = fields.Char()
