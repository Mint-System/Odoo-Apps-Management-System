from odoo import fields, models, api

class Management(models.Model):
    _name = "mgmt.task"
    _description = "Task"    
    name = fields.Char("Title", required=True)
    description = fields.Text("Description")   