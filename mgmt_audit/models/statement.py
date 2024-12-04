import logging

from odoo import fields, models

_logger = logging.getLogger(__name__)


class MgmtStatement(models.Model):
    _name = "mgmt.statement"
    _description = "Mgmt Statement"

    name = fields.Char(required=True)
    risk_id = fields.Many2one("mgmt.risk")
    audit_id = fields.Many2one("mgmt.audit", cascade="delete")
    requirement_id = fields.Many2one("mgmt.requirement")
    nonconformity_id = fields.Many2one("mgmt.nonconformity")
    recommendation_id = fields.Many2one("mgmt.recommendation")
    attachment_id = fields.Many2one("ir.attachment")
