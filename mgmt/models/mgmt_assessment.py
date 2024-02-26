from odoo import fields, models, api

class Management(models.Model):
    _inherit = ["mail.thread", "mail.activity.mixin"]
    _name = "mgmt.assessment"
    _description = "Assessment"    
    name = fields.Char("Title", required=True)
    description = fields.Text("Description")
    date_begin = fields.Datetime("Start Date")
    date_end = fields.Datetime("End Date")
    comment = fields.Html("Comment")  
    author_id = fields.Many2one("res.partner", 
      string="Author")  
    hazard_history_id = fields.One2many(
        'mgmt.hazard.history', 'assessment_id',          
        string="Hazard history")      