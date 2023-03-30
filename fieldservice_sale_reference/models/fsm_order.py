# © 2023 Solvos Consultoría Informática (<http://www.solvos.es>)
# License AGPL-3 - See http://www.gnu.org/licenses/agpl-3.0.html

from odoo import fields, models


class FSMOrder(models.Model):
    _inherit = "fsm.order"

    sale_reference = fields.Char(related="sale_id.client_order_ref", string="Reference")
