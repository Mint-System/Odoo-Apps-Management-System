# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).

import logging

from odoo import fields, models

_logger = logging.getLogger(__name__)


class MaintenanceEquipmentCategory(models.Model):
    _inherit = ["maintenance.equipment.category"]

    owner_id = fields.Many2one("res.partner")
