from odoo import fields, models, api

class Management(models.Model):
    _inherit = ["mail.thread", "mail.activity.mixin"]
    _name = "mgmt.paragraph"
    _description = "Paragraph"    
    name = fields.Char("Title", required=True)
    description = fields.Html("Description")
    parent_id = fields.Many2one("mgmt.paragraph", "parent_id")
    requirement_ids = fields.Many2many("mgmt.requirement", 
      string="Requirement")    