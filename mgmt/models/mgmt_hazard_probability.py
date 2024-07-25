from odoo import fields, models


class Management(models.Model):
    _name = "mgmt.hazard.probability"
    _description = "Hazard probability"
    name = fields.Char("Title", required=True)
    value = fields.Integer("Value")
    description = fields.Text("Description")
