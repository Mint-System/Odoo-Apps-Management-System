import logging

from odoo import api, fields, models

_logger = logging.getLogger(__name__)


MODEL_SELECTION = [
    ("res.partner", "Contact"),
    ("product.product", "Product"),
    ("hr.employee", "Employee"),
    ("maintenance.equipment", "Inventory"),
    ("maintenance.equipment.category", "Inventory Category"),
]


class MgmtAsset(models.Model):
    _name = "mgmt.asset"
    _description = "Mgmt Asset"

    name = fields.Char(compute="_compute_name", store=True, readonly=False)
    ref = fields.Reference(
        selection="_get_ref_selection", string="Reference", required=True
    )

    @api.model
    def _get_ref_selection(self):
        model_selection = [model[0] for model in MODEL_SELECTION]
        models = self.env["ir.model"].sudo().search([("model", "in", model_selection)])
        return [(model.model, model.name) for model in models]

    @api.depends("ref")
    def _compute_name(self):
        for rec in self:
            if ref.ref:
                model = self.env["ir.model"].search(
                    [("model", "=", rec.ref._name)], limit=1
                )
                record_ref = self.env[model.model].browse(rec.ref.id)
                rec.name = f"{record_ref.display_name} ({model.name})"
            else:
                rec.name = ""
