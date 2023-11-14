from odoo import fields, models
class Management(models.Model):
    _name = "mgmt.audit"
    _description = "Audit"    
    name = fields.Char("Title", required=True)  
    reference = fields.Char("Referenz")  
    date_begin = fields.Datetime("Start Date")
    date_end = fields.Datetime("End Date")
    comment = fields.Html("Comment")  
    category_id = fields.Many2one("mgmt.audit.category", 
      string="Category")
    type_id = fields.Many2one("mgmt.audit.type", 
      string="Type")
    auditor_id = fields.Many2one("res.partner", 
      string="Auditor")
    author_id = fields.Many2one("res.partner", 
      string="Author")  

    nonconformity_ids = fields.Many2many("mgmt.nonconformity", 
      string="Nonconformity")    

    compliancestatement_ids = fields.Many2many("mgmt.compliancestatement", 
      string="Compliancestatement") 
       
    document_ids = fields.Many2many("mgmt.document", 
      string="Documents")

    participant_ids = fields.Many2many ("res.partner", 
      string="Participant",
      relation="audit_participant_rel",
      column1="audit_id",
      column2="partner_id") 

    audit_team_member_ids = fields.Many2many("res.partner", 
      string="Audit Team Member",
      relation="audit_team_member_rel",
      column1="audit_id", 
      column2="partner_id")