from odoo import fields, models
class Management(models.Model):
    _name = "mgmt.compliancestatement"
    _description = "Compliancestatement"    
    name = fields.Char("Title")
    description = fields.Text("Description")
    document_id = fields.Many2one("mgmt.document", 
      string="Document")
    requirement_id = fields.Many2one("mgmt.requirement", 
      string="Requirement")
    audit_id = fields.Many2one('mgmt.audit', 
        string="Audit")       
    requirement_name = fields.Char(
        string="Requirement Name",
        related="requirement_id.name")
    requirement_description = fields.Text(
        string="Requirement Description", 
        related="requirement_id.description")
