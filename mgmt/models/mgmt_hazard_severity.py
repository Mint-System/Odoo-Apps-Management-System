from odoo import fields, models, api

class Management(models.Model):
    _name = "mgmt.hazard.severity"
    _description = "Hazard severity"    
    name = fields.Char("Title", required=True)
    value = fields.Integer("Value")
    description = fields.Text("Description")