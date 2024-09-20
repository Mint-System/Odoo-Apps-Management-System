import logging

from odoo import api, fields, models

_logger = logging.getLogger(__name__)


class MgmtRecommendation(models.Model):
    _inherit = "mgmt.recommendation"
    _description = "Mgmt Recommendation"

    name = fields.Char(required=True)
    task_ids = fields.One2many("project.task", "recommendation_id")

    @api.model
    def _get_default_project_id(self):
        project = self.env.ref("mgmt_audit_project.mgmt_project", raise_if_not_found=False)
        if project:
            return project.id
        return self.env['project.project'].search([], limit=1).id

    project_id = fields.Many2one('project.project', required=True, default=_get_default_project_id, ondelete='cascade')
