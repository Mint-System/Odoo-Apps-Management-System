import logging

from odoo import api, fields, models

_logger = logging.getLogger(__name__)


class MgmtAudit(models.Model):
    _name = "mgmt.audit"
    _inherit = ["mail.thread", "mail.activity.mixin"]
    _description = "Mgmt Audit"

    name = fields.Char(required=True, tracking=True)
    description = fields.Html()
    type = fields.Selection(
        [
            ("internal", "Internal"),
            ("external", "External"),
        ],
        tracking=True,
    )
    planned_date = fields.Date(tracking=True)
    stage_id = fields.Many2one(
        "mgmt.audit.stage",
        tracking=True,
        required=True,
        default=lambda self: self.env.ref("mgmt_audit.audit_stage_draft").id,
        group_expand="_read_group_stage_ids",
        inverse = "_inverse_stage_id",
    )
    responsible_id = fields.Many2one("hr.employee", tracking=True)
    statement_ids = fields.One2many("mgmt.statement", "audit_id")
    auditor_ids = fields.Many2many("res.partner")

    def _inverse_stage_id(self):
        if self.stage_id.code == 'done':
            for audit in self:
                risk_ids = audit.statement_ids.risk_id + audit.statement_ids.requirement_id.risk_ids
                risk_ids._compute_last_review_date()

    @api.model
    def _read_group_stage_ids(self, stages, domain):
        return self.env["mgmt.audit.stage"].search([])
