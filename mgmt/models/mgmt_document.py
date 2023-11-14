from odoo import fields, models
class Management(models.Model):
    _name = "mgmt.document"
    _description = "Document"    
    name = fields.Char("Title", required=True)
    description = fields.Text("Description")