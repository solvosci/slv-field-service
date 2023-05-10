# © 2023 Solvos Consultoría Informática (<http://www.solvos.es>)
# License AGPL-3 - See http://www.gnu.org/licenses/agpl-3.0.html
from odoo import models


class SaleOrder(models.Model):
    _inherit = "sale.order"

    def _prepare_fsm_values(self, **kwargs):
        res = super(SaleOrder, self)._prepare_fsm_values(**kwargs)
        template_id = kwargs.get("template_id", False)
        template_ids = kwargs.get("template_ids", [template_id])
        templates = self.env["fsm.template"].search([("id", "in", template_ids)])
        note = ""
        for template in templates:
            if template.collaborator_instructions:
                note += template.collaborator_instructions
        res["collaborator_todo"] = note
        return res
