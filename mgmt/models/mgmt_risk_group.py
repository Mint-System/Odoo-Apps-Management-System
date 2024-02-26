from odoo import fields, models, api

class Management(models.Model):
    _inherit = ["mail.thread", "mail.activity.mixin"]
    _name = "mgmt.risk.group"
    _description = "Risk group"    
    name = fields.Char("Title", required=True)
    description = fields.Text("Description")