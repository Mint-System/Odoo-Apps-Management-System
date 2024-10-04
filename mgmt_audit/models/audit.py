import logging

from odoo import api, fields, models

_logger = logging.getLogger(__name__)


class MgmtAudit(models.Model):
    _name = "mgmt.audit"
    _description = "Mgmt Audit"

    name = fields.Char(required=True)
    requirement_ids = fields.Many2many("mgmt.requirement")
    type = fields.Selection(
        [
            ("internal", "Internal"),
            ("external", "External"),
        ]
    )
    planned_date = fields.Date()
    stage_id = fields.Many2one(
        "mgmt.audit.stage",
        required=True,
        default=lambda self: self.env.ref("mgmt_audit.audit_stage_draft").id,
        group_expand="_read_group_stage_ids",
    )
    responsible_id = fields.Many2one("hr.employee")
    statement_ids = fields.Many2many("mgmt.statement")
    auditor_ids = fields.Many2many("res.partner")

    @api.model
    def _read_group_stage_ids(self, stages, domain, order):
        return self.env["mgmt.audit.stage"].search([])

    def action_create_revision(self):
            for audit in self:
                new_audit = audit.copy({
                    'name': f"{audit.name} (Revision)",
                    'stage_id': self.env.ref('mgmt_audit.audit_stage_draft').id,
                })
            return {
                'type': 'ir.actions.act_window',
                'name': 'New Audit Revision',
                'view_mode': 'form',
                'res_model': 'mgmt.audit',
                'res_id': new_audit.id,
                'target': 'current',
            }
