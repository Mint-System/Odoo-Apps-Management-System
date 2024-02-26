from odoo import fields, models, api

class Management(models.Model):
    _inherit = ["mail.thread", "mail.activity.mixin"]
    _name = "mgmt.risk"
    _description = "Risk"    
    name = fields.Char("Title", required=True)
    description = fields.Text("Description")

    group_name = fields.Many2one("mgmt.risk.group.name", 
        string="Risk group") 

    group_id = fields.Many2one("mgmt.risk.group.id", 
        string="Risk group") 
    
    hazard_ids = fields.One2many("mgmt.hazard", "risk_id", string="Hazards")