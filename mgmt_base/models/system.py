from odoo import fields, models


class MgmtSystem(models.Model):
    _name = "mgmt.system"
    _description = "Mgmt System"

    name = fields.Char("System", required=True)
    company_id = fields.Many2one(
        "res.company", "Company", default=lambda self: self.env.company
    )
