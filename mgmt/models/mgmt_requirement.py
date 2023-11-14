from odoo import fields, models
class Management(models.Model):
    _name = "mgmt.requirement"
    _description = "Requirement"    
    name = fields.Char("Title")
    description = fields.Text("Description")