# © 2023 Solvos Consultoría Informática (<http://www.solvos.es>)
# License AGPL-3 - See http://www.gnu.org/licenses/agpl-3.0.html

from odoo import api, fields, models
from odoo.osv import expression


class FSMOrder(models.Model):
    _inherit = "fsm.order"

    sale_reference = fields.Char(related="sale_id.client_order_ref", string="Reference")
    display_name = fields.Char(compute="_compute_display_name", related="")

    def _compute_display_name(self):
        orders_w_sale = self.filtered(lambda x: x.sale_reference)
        for order in orders_w_sale:
            order.display_name = "{} - {}".format(order.name, order.sale_reference)
        for order in (self - orders_w_sale):
            order.display_name = order.name

    def name_get(self):
        result = super().name_get()
        new_result = []

        for order in result:
            rec = self.browse(order[0])
            name = rec.display_name
            new_result.append((rec.id, name))
        return new_result

    @api.model
    def _name_search(self, name, args=None, operator='ilike', limit=100, name_get_uid=None):
        args = args or []
        domain = []
        # TODO negative operators handling
        if name:
            domain = ['|', ('name', operator, name), ('sale_reference', operator, name)]
        return self._search(expression.AND([domain, args]), limit=limit, access_rights_uid=name_get_uid)
