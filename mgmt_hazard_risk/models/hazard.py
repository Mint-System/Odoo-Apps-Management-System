import logging

from odoo import fields, models

_logger = logging.getLogger(__name__)


class MgmtHazard(models.Model):
    _inherit = "mgmt.hazard"

    severity_id = fields.Many2one("mgmt.severity")
    probability_id = fields.Many2one("mgmt.probability")

    def action_create_revision(self):
        for hazard in self:
            new_hazard = hazard.copy({
                'name': f"{hazard.name} (Revision)",
            })
            return {
                'type': 'ir.actions.act_window',
                'name': 'New Hazard Revision',
                'view_mode': 'form',
                'res_model': 'mgmt.hazard',
                'res_id': new_hazard.id,
                'target': 'current',
            }
