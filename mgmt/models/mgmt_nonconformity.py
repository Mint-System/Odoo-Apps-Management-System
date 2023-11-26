from odoo import fields, models
class Management(models.Model):
    _name = "mgmt.nonconformity"
    _description = "Nonconformity"    
    name = fields.Char("Title", required=True)
    description = fields.Text("Description")
    audit_ids = fields.Many2many('mgmt.audit', 
        string="Audits")   
    audit_name = fields.Char(
        string="Audit",
        related="audit_ids.name")    