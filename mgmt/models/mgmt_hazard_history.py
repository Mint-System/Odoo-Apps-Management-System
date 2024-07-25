from odoo import fields, models


class Management(models.Model):
    _inherit = ["mail.thread", "mail.activity.mixin"]
    _name = "mgmt.hazard.history"
    _description = "Hazard history"
    name = fields.Char("Title", required=True)
    description = fields.Text("Description")
    hazard_id = fields.Many2one("mgmt.hazard", string="Hazard")
    probability_id = fields.Many2one("mgmt.hazard.probability", string="Probability")
    severity_id = fields.Many2one("mgmt.hazard.severity", string="Severity")
    assessment_id = fields.Many2one("mgmt.assessment", string="Assessment")
    risk_name = fields.Char(
        string="Risk Name", related="hazard_id.risk_id.name", store=True
    )

    assessment_id = fields.Many2one("mgmt.assessment", string="Assessment")
    assessment_date = fields.Datetime(
        string="Datum", store=True, related="assessment_id.date_begin"
    )
