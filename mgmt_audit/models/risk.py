import logging

from odoo import fields, models

_logger = logging.getLogger(__name__)


class MgmtRisk(models.Model):
    _inherit = "mgmt.risk"

    last_review_date = fields.Date(compute="_compute_last_review_date", store=True)
    statement_ids = fields.One2many("mgmt.statement", "risk_id")

    def _compute_last_review_date(self):
        """
        Date of the last audit. Compute method is called when planned_date is changed.
        """
        for risk in self:
            audit_ids = risk.requirement_ids.statement_ids.audit_id + risk.statement_ids.audit_id
            audit_dates = audit_ids.mapped("planned_date")
            risk.last_review_date = max(audit_dates) if audit_dates else False

    def create_audit_with_risk_statements(self):
        """Create an audit with selected risks as statements."""
        if self.requirement_ids:
            audit = self.env["mgmt.audit"].create(
                {
                    "name": "Risk Audit",
                    "planned_date": fields.Date.today(),
                }
            )

            statement_id = []
            for risk in self:
                for requirement in risk.requirement_ids:
                    statement_id.append(
                        self.env["mgmt.statement"].create(
                            {
                                "name": requirement.name,
                                "audit_id": audit.id,
                                "requirement_id": requirement.id,
                                "risk_id": risk.id,
                            }
                        )
                    )

            return {
                "type": "ir.actions.act_window",
                "name": "Audit",
                "res_model": "mgmt.audit",
                "view_mode": "form",
                "res_id": audit.id,
                "context": {"default_statement_ids": statement_id},
            }
