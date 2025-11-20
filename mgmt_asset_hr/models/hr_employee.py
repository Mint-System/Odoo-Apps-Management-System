# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).

import logging

from odoo import fields, models

_logger = logging.getLogger(__name__)


class HrEmployee(models.Model):
    _inherit = ["hr.employee"]

    owner_id = fields.Many2one("res.partner")
