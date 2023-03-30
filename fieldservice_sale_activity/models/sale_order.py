# © 2023 Solvos Consultoría Informática (<http://www.solvos.es>)
# License AGPL-3 - See http://www.gnu.org/licenses/agpl-3.0.html

from odoo import models


class SaleOrder(models.Model):
    _inherit = "sale.order"

    def _field_service_generation(self):
        res = super()._field_service_generation()

        for record in res:
            activity_list = []
            # Only those products that create a one FSM order per sale
            #  order does not copy their activities
            for temp_activity in record.sale_id.order_line.filtered(
                lambda x: x.product_id.field_service_tracking == "sale"
            ).product_id.fsm_order_template_id.temp_activity_ids:
                activity_list.append(
                    (
                        0,
                        0,
                        self._prepare_activity_dict(temp_activity),
                    )
                )
            record.order_activity_ids = activity_list

        return res

    def _prepare_activity_dict(self, activity_id):
        return {
            "name": activity_id.name,
            "required": activity_id.required,
            "ref": activity_id.ref,
            "state": activity_id.state,
        }
