from odoo import fields, models, api

class Management(models.Model):
    _name = "mgmt.document"
    _description = "Document"    
    name = fields.Char("Title", required=True)
    description = fields.Text("Description")
    mid= fields.Integer("MID")    
    parent_id = fields.Many2one("mgmt.document", "Hierarchy")
    child_ids = fields.One2many("mgmt.document", "parent_id", "Children")   
    url = fields.Char(string='URL')
    owner_id = fields.Many2one("hr.employee", 
      string="Owner")
    code = fields.Char("Code")
    category_id = fields.Many2one("mgmt.document.category", 
      string="Category")
    version = fields.Char(string='Version')