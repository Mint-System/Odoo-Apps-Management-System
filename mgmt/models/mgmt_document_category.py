from odoo import fields, models
class Management(models.Model):
    _name = "mgmt.document.category"
    _description = "Document Category"    
    name = fields.Char("Title", required=True)