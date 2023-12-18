from odoo import fields, models, api

class Management(models.Model):
    _inherit = ["mail.thread", "mail.activity.mixin"]
    _name = "mgmt.docustructure"
    _description = "Docustructure"    
    name = fields.Char("Title", required=True)
    description = fields.Html("Description")
    parent_id = fields.Many2one("mgmt.docustructure",
      string="Hierarchy")
    document_id = fields.Many2one("mgmt.document",
      string="Document")