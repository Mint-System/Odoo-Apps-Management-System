from odoo import fields, models
class Management(models.Model):
    _name = "mgmt.nonconformity"
    _description = "Nonconformity"    
    name = fields.Char("Title", required=True)
    description = fields.Text("Description")    