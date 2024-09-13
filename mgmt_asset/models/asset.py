import logging

from odoo import fields, models

_logger = logging.getLogger(__name__)


class MgmtAsset(models.Model):
    _name = "mgmt.asset"
    _description = "Mgmt Asset"

    name = fields.Char()
    model_name = fields.Selection([
        ('product.product', 'Product'),
        ('maintenance.equipment', 'Inventory'),
        ('res.partner', 'Contact')
    ])

    model_id = fields.Many2one('ir.model')
    res_id = fields.Integer(required=True)
