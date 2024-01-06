from odoo import fields, models, api

class Management(models.Model):
    _inherit = ["mail.thread", "mail.activity.mixin"]
    _name = "mgmt.paragraph"
    _description = "Paragraph"    
    name = fields.Char("Title")
    description = fields.Text("Description")
    parent_id = fields.Many2one("mgmt.paragraph", "parent_id")
    docustructure_id = fields.Many2one("mgmt.docustructure",
      string="Docustructure")
    document_id = fields.Many2one('mgmt.document', string="Source", store=True, related="docustructure_id.document_id")
    requirement_ids = fields.Many2many("mgmt.requirement", 
      string="Requirement")
    display_name = fields.Char(string="Display Name", compute="_compute_display_name", store=True)  

    @api.depends("docustructure_id.number", "name")
    def _compute_display_name(self):
        for record in self:
            paragraph_name = record.name if record.name else ""
            record.display_name = f"{record.docustructure_id.number} {paragraph_name}"