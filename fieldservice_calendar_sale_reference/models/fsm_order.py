# © 2023 Solvos Consultoría Informática (<http://www.solvos.es>)
# License AGPL-3 - See http://www.gnu.org/licenses/agpl-3.0.html
from odoo import models


class FSMOrder(models.Model):
    _inherit = "fsm.order"
    
    def _prepare_calendar_event(self):
        vals = super(FSMOrder, self)._prepare_calendar_event()
        if self.name and self.sale_reference:
            vals["name"] = '%s - %s' % (self.name, self.sale_reference)
        return vals
