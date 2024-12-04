import logging

from odoo import api, fields, models

_logger = logging.getLogger(__name__)


class MgmtRisk(models.Model):
    _inherit = "mgmt.risk"

    last_review_date = fields.Date(compute="_compute_last_review_date", stored=True)

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
