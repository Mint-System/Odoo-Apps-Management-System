import logging

from odoo import api, fields, models

_logger = logging.getLogger(__name__)


class MgmtRisk(models.Model):
    _name = "mgmt.risk"
    _description = "Mgmt Risk"

    name = fields.Char(required=True)
    description = fields.Html()
    risk_owner_id = fields.Many2one("res.users", required=True)
    severity_id = fields.Many2one("mgmt.severity", required=True)
    revision_risk_ids = fields.One2many("mgmt.risk", "head_risk_id")
    head_risk_id = fields.Many2one("mgmt.risk")
    probability_id = fields.Many2one("mgmt.probability", required=True)
    risk_score = fields.Float(compute="_compute_risk_score", store=True)
    color = fields.Integer(compute="_compute_color", store=True)
    stage = fields.Many2one(
        "mgmt.risk.stage",
        required=True,
        default=lambda self: self.env.ref("mgmt_risk.stage_evaluate").id,
        group_expand="_read_group_stage_ids",
    )
    system_id = fields.Many2one("mgmt.system")
    requirement_ids = fields.Many2many("mgmt.requirement", "risk_ids")

    @api.model
    def _read_group_stage_ids(self, stages, domain, order):
        return self.env["mgmt.risk.stage"].search([])

    @api.depends("severity_id", "probability_id")
    def _compute_risk_score(self):
        for record in self:
            severity = record.severity_id.value if record.severity_id else 0
            probability = record.probability_id.value if record.probability_id else 0

            formula = self.env.company.mgmt_risk_formula

            if formula == "multiply":
                record.risk_score = severity * probability
            elif formula == "sum":
                record.risk_score = severity + probability
            else:
                record.risk_score = 0
