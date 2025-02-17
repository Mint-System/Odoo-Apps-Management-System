import logging

from odoo import _, api, fields, models

_logger = logging.getLogger(__name__)


class MgmtRisk(models.Model):
    _name = "mgmt.risk"
    _inherit = ["mail.thread", "mail.activity.mixin"]
    _description = "Mgmt Risk"

    name = fields.Char(required=True, tracking=True)
    description = fields.Html()
    risk_owner_id = fields.Many2one("res.users", required=True, tracking=True)
    hazard_ids = fields.Many2many("mgmt.hazard")
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
            ("redcued", "Reduced"),
            ("transfered", "Transfered"),
            ("eliminated", "Eliminiated"),
        ],
    )

    revision_risk_ids = fields.One2many("mgmt.risk", "head_risk_id")
    revision_count = fields.Integer(default=0)
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

    def _compute_display_name(self):
        for rec in self:
            if rec.head_risk_id:
                rec.display_name = f"{rec.name} [{str(rec.revision_count)}]"
            else:
                rec.display_name = rec.name

    @api.model
    def _read_group_stage_ids(self, stages, domain):
        return self.env["mgmt.risk.stage"].search([])

    @api.depends("severity_id", "probability_id")
    def _compute_risk_score(self):
        for rec in self:
            severity = rec.severity_id.value if rec.severity_id else 0
            probability = rec.probability_id.value if rec.probability_id else 0

            formula = self.env.company.mgmt_risk_formula

            if formula == "multiply":
                rec.risk_score = severity * probability
            elif formula == "sum":
                rec.risk_score = severity + probability
            else:
                rec.risk_score = 0

    @api.depends("severity_id", "probability_id")
    def _compute_risk_combination_id(self):
        for rec in self:
            risk_combination_id = self.env["mgmt.risk.combination"].search(
                [
                    ("severity_id", "=", rec.severity_id.id),
                    ("probability_id", "=", rec.probability_id.id),
                ],
                limit=1,
            )
            rec.risk_combination_color = risk_combination_id.color
            rec.risk_combination_id = risk_combination_id

    def action_create_revision(self):
        self.ensure_one()

        # Create a copy of risk and set head
        risk_revision = self.copy()
        self.revision_count += 1
        risk_revision.write({"head_risk_id": self.id})

        # Client reload and then success notification
        action = {
            "type": "ir.actions.client",
            "tag": "display_notification",
            "params": {
                "type": "success",
                "title": _("Revision Created"),
                "message": _("A new revision has been created."),
                "sticky": True,
                "next": {
                    "type": "ir.actions.client",
                    "tag": "reload",
                },
            },
        }

        return action
