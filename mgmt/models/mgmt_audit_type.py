from odoo import fields, models


class Management(models.Model):
    _name = "mgmt.audit.type"
    _description = "Audit Type"
    name = fields.Char("Title", required=True)
