import logging

from odoo import api, fields, models

_logger = logging.getLogger(__name__)


class MgmtRisk(models.Model):
    _inherit = "mgmt.risk"

    last_review_date = fields.Date(compute="_compute_last_review_date", store=True)

    @api.depends(
        "requirement_ids",
        "requirement_ids.statement_ids",
        "requirement_ids.statement_ids.audit_id",
    )
    def _compute_last_review_date(self):
        """
        Date of the last audit.
        Connection is risk_id -> requirement_ids ->
        statement_ids -> audit_id:planned_date.
        """

        for risk in self:
            audit_dates = risk.requirement_ids.statement_ids.audit_id.mapped(
                "planned_date"
            )
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
