from odoo import fields, models, api

class Management(models.Model):
    _name = "mgmt.meeting"
    _description = "Meeting"    
    name = fields.Char("Title", required=True)
    description = fields.Text("Description")   