from odoo import fields, models
class Management(models.Model):
    _name = "mgmt.action"
    _description = "Action"    
    name = fields.Char("Title", required=True)
    date_deadline = fields.Date("Deadline")
    date_closed = fields.Datetime("Closed Date", readonly=True)
    responsible_id = fields.Many2one("res.partner",
        string="Responsible")