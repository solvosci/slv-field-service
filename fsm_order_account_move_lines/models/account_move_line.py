# © 2023 Solvos Consultoría Informática (<http://www.solvos.es>)
# License AGPL-3 - See http://www.gnu.org/licenses/agpl-3.0.html
from odoo import models, fields, api


class AccountMoveLine(models.Model):
    _inherit = "account.move.line"

    fsm_order_id = fields.Many2one("fsm.order")
    scheduled_date_start = fields.Datetime(
        related='fsm_order_id.scheduled_date_start',
        store=True)
    
    # @api.depends('ref')
    # def _compute_fsm_order_id(self):
    #     for order in self:
    #         order.fsm_order_id = '%s - %s' % (order.fsm_order_id, order.ref)

    # def _prepare_analytic_line(self):
    #     prepare = super(AccountMoveLine, self)._prepare_analytic_line()
    #     if self.fsm_order_id:
    #         prepare["fsm_order_id"] = self.fsm_order_id.id
    #     return prepare
    
    # def _add_lines_to_exchange_difference_vals(lines, exchange_diff_move_vals):
    #     create = super(AccountMoveLine, lines)._add_lines_to_exchange_difference_vals(lines, exchange_diff_move_vals)
    #     if lines.fsm_order_id:
    #         create["fsm_order_id"] = lines.fsm_order_id.id
    #     return create

