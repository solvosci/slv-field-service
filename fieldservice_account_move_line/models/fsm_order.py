# © 2023 Solvos Consultoría Informática (<http://www.solvos.es>)
# License AGPL-3 - See http://www.gnu.org/licenses/agpl-3.0.html
from odoo import models, fields


class FSMOrder(models.Model):
    _inherit = "fsm.order"

    account_move_line_ids = fields.One2many(
        "account.move.line",
        "fsm_order_id")
