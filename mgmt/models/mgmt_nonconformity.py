from odoo import fields, models
class Management(models.Model):
    _name = "mgmt.nonconformity"
    _description = "Nonconformity"    
    name = fields.Char("Title", required=True)
    description = fields.Text("Description")
    code = fields.Char("Code")
    audit_id = fields.Many2one('mgmt.audit', string="Audit")