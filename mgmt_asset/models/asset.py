import logging

from odoo import api, fields, models

_logger = logging.getLogger(__name__)

class MgmtAsset(models.Model):
    _name = "mgmt.asset"
    _description = "Mgmt Asset"

    name = fields.Char(compute="_compute_name", store=True, readonly=False)
    model_name = fields.Selection(
        [
            ("res.partner", "Contact"),
            ("product.product", "Product"),
            ("hr.employee", "Employee"),
            ("maintenance.equipment", "Inventory"),
            ("maintenance.equipment.category", "Inventory Category"),
        ],
        required=True,
    )

    model_id = fields.Many2one("ir.model", compute="_compute_model_id", store=True)
    res_id = fields.Integer(required=True)

    @api.depends("model_name")
    def _compute_model_id(self):
        for record in self:
            if record.model_name:
                model = self.env["ir.model"].search([("model", "=", record.model_name)], limit=1)
                record.model_id = model.id if model else False
            else:
                record.model_id = False

    @api.depends("model_name", "model_id", "res_id")
    def _compute_name(self):
        for record in self:
            if record.model_name and record.res_id:
                linked_record = self.env[record.model_name].browse(record.res_id)
                record.name = linked_record.display_name if linked_record else "Unknown"
            else:
                record.name = "Unknown"
