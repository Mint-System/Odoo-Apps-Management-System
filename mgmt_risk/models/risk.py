import logging

from odoo import api, fields, models

_logger = logging.getLogger(__name__)


class MgmtRisk(models.Model):
    _name = "mgmt.risk"
    _inherit = ["mail.thread", "mail.activity.mixin"]
    _description = "Mgmt Risk"

    name = fields.Char(required=True, tracking=True)
    description = fields.Html()
    risk_owner_id = fields.Many2one("res.users", required=True, tracking=True)
    hazard_ids = fields.Many2many("mgmt.hazard")
    revision_risk_ids = fields.One2many("mgmt.risk", "head_risk_id")
    head_risk_id = fields.Many2one("mgmt.risk", tracking=True)

    severity_id = fields.Many2one("mgmt.severity", required=True, tracking=True)
    severity_color = fields.Integer(related="severity_id.color")

    probability_id = fields.Many2one("mgmt.probability", required=True, tracking=True)
    probability_color = fields.Integer(related="probability_id.color")

    color = fields.Integer(compute="_compute_color", store=True)

    risk_combination_id = fields.Many2one(
        "mgmt.risk.combination", compute="_compute_risk_combination_id"
    )
    risk_combination_color = fields.Integer(compute="_compute_risk_combination_id")
    risk_score = fields.Float(compute="_compute_risk_score", store=True)

    stage = fields.Many2one(
        "mgmt.risk.stage",
        required=True,
        tracking=True,
        default=lambda self: self.env.ref("mgmt_risk.stage_evaluate").id,
        group_expand="_read_group_stage_ids",
    )
    system_id = fields.Many2one("mgmt.system")
    risk_acceptance = fields.Selection(
        [
            ("accepted", "Accepted"),
        ],
    )

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

    @api.depends("severity_id", "probability_id")
    def _compute_risk_combination_id(self):
        for record in self:
            risk_combination_id = self.env["mgmt.risk.combination"].search(
                [
                    ("severity_id", "=", record.severity_id.id),
                    ("probability_id", "=", record.probability_id.id),
                ],
                limit=1,
            )
            rec.risk_combination_color = risk_combination_id.color
            rec.risk_combination_id = risk_combination_id
