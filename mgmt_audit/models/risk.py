import logging

from odoo import models

_logger = logging.getLogger(__name__)


class MgmtRisk(models.Model):
    _inherit = "mgmt.risk"

    last_review_date = fields.Date(compute="_compute_last_review_date")

    def _compute_last_review_date(self):
        """
        Date of the last audit.
        Connection is risk_id -> requirement_ids -> statement_ids -> audit_id:planned_date.
        """

        for risk in self:
            risk.last_review_date = (
                risk.requirement_ids.mapped("statement_ids")
                .mapped("audit_id")
                .mapped("planned_date")
                .max()
            )