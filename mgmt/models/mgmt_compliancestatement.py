from odoo import fields, models
class Management(models.Model):
    _name = "mgmt.compliancestatement"
    _description = "Compliancestatement"    
    name = fields.Char("Title")
    description = fields.Html("Description")
    document_id = fields.Many2one("mgmt.document", 
      string="Document")
    requirement_id = fields.Many2one("mgmt.requirement", 
      string="Requirement")
    audit_ids = fields.Many2many('mgmt.audit', 
        string="Audits")   
    audit_name = fields.Char(
        string="Audit",
        related="audit_ids.name")    
    audit_category_id = fields.Many2one('mgmt.audit.category',
        string="Category",
        related="audit_ids.category_id")
    requirement_name = fields.Char(
        string="Requirement Name",
        related="requirement_id.name")
    requirement_description = fields.Text(
        string="Requirement Description",
        related="requirement_id.description")
