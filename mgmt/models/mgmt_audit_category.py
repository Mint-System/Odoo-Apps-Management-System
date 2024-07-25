from odoo import fields, models


class Management(models.Model):
    _name = "mgmt.audit.category"
    _description = "Audit Category"
    name = fields.Char("Title", required=True)
