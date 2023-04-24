# © 2023 Solvos Consultoría Informática (<http://www.solvos.es>)
# License AGPL-3 - See http://www.gnu.org/licenses/agpl-3.0.html
from odoo import models


class SaleOrder(models.Model):
    _inherit = "sale.order"

    def _prepare_fsm_values(self, **kwargs):
        prepare = super(SaleOrder, self)._prepare_fsm_values(**kwargs)
        if self.commitment_date:
            prepare["scheduled_date_start"] = self.commitment_date
        return prepare
