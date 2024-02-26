from odoo import fields, models, api

class Management(models.Model):
    _inherit = ["mail.thread", "mail.activity.mixin"]
    _name = "mgmt.hazard"
    _description = "Hazard"    
    name = fields.Char("Title", required=True)
    description = fields.Text("Description")
    probability_id = fields.Many2one("mgmt.hazard.probability", 
        string="Probability") 
    severity_id = fields.Many2one("mgmt.hazard.severity", 
        string="Severity")   
    audit_id = fields.Many2one('mgmt.audit', string="Audit")
    risk_id = fields.Many2one('mgmt.risk', string="Risk")