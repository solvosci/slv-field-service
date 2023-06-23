# © 2023 Solvos Consultoría Informática (<http://www.solvos.es>)
# License AGPL-3 - See http://www.gnu.org/licenses/agpl-3.0.html
from odoo import models, fields, api


class AccountMoveLine(models.Model):
    _inherit = "account.move.line"

    fsm_order_id = fields.Many2one("fsm.order", check_company=True)
    scheduled_date_start = fields.Datetime(   
        related='fsm_order_id.scheduled_date_start',
        store=True)
