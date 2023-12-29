from odoo import fields, models, api

class Management(models.Model):
    _inherit = ["mail.thread", "mail.activity.mixin"]
    _name = "mgmt.docustructure"
    _description = "Docustructure"    
    name = fields.Char("Title")
    number = fields.Char("Number")
    parent_id = fields.Many2one("mgmt.docustructure",
      string="Parent")
    document_id = fields.Many2one("mgmt.document",
      string="Document")   
    display_name = fields.Char(string="Display Name", compute="_compute_display_name", store=True)

    @api.depends("number", "name")
    def _compute_display_name(self):
        for record in self:
            record.display_name = f"{record.number} {record.name}"