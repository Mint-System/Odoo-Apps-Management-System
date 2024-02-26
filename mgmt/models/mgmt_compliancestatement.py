from odoo import fields, models, api

class Management(models.Model):
    _name = "mgmt.compliancestatement"
    _description = "Compliancestatement"   
    _order = 'sort asc' 
    name = fields.Char("Title")
    description = fields.Text("Description")
    document_id = fields.Many2one("mgmt.document", 
      string="Document")
    requirement_id = fields.Many2one("mgmt.requirement", 
      string="Requirement")
    audit_id = fields.Many2one('mgmt.audit', 
        string="Audit")    
    audit_date = fields.Datetime(
        string="Datum",
        store=True,
        related="audit_id.date_begin")
    requirement_name = fields.Char(
        string="Requirement Name",
        related="requirement_id.name")
    requirement_description = fields.Text(
        string="Requirement Description", 
        related="requirement_id.description")    
    requirement_paragraph_ids = fields.Many2many("mgmt.paragraph",
        string="Paragraphs",
        related="requirement_id.paragraph_ids",)
        # domain="[('document_id', '=', 43977)]")
    requirement_paragraph_display_name = fields.Char(
        string="Paragraph",
        store=True,
        related="requirement_paragraph_ids.display_name")       
    requirement_paragraph_document_id_name = fields.Char(
        string="Source",
        store=True, 
        related="requirement_paragraph_ids.document_id.name")
    requirement_paragraph_document_id_id = fields.Many2one("mgmt.document",
        string="Paragraph Document ID",
        store=True,
        related="requirement_paragraph_ids.document_id")
    sort = fields.Char(string="Sort", compute="_compute_sort", store=True)

    @api.depends("name", "description")
    def _compute_sort(self):
        for record in self:
            if record.requirement_id.paragraph_ids:                
              record.sort = f"{record.requirement_id.paragraph_ids[0].id}"
            else:
              record.sort = f""