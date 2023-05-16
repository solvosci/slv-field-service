# © 2023 Solvos Consultoría Informática (<http://www.solvos.es>)
# License AGPL-3 - See http://www.gnu.org/licenses/agpl-3.0.html
from odoo import models, fields, api


class FSMOrderSalary(models.Model):
    _name = "fsm.order.salary"
    _description = "Field Service Order Salary"

    # TODO fill this field // use display_name if needed
    name = fields.Char()
    fsm_order_id = fields.Many2one('fsm.order', required=True)
    sale_id = fields.Many2one("sale.order")
    fsm_person_id = fields.Many2one('fsm.person', required=True)
    sequence = fields.Integer()
    vehicle = fields.Boolean()
    payments_salary = fields.Monetary(string='Salary', required=True)
    payments_km = fields.Monetary(string='Km')
    payments_diets = fields.Monetary(string='Diets')
    payments_advance = fields.Monetary(string='Advance')
    net_salary = fields.Monetary(currency_field='currency_id',
        compute='_compute_net_salary',
        string='Net Salary', store=True)
    currency_id = fields.Many2one('res.currency', 'Currency', required=True,
        default=lambda self: self.env.company.currency_id.id)
    scheduled_date_start = fields.Datetime(
        related='fsm_order_id.scheduled_date_start',
        store=True)
    location_id = fields.Many2one(
        "fsm.location", 
        related='fsm_order_id.location_id',
        string="Location", 
        index=True, 
        store=True)
    customer_id = fields.Many2one('res.partner', string="Contact")
    task = fields.Char()
    task_date = fields.Datetime()
    vat = fields.Char(related='fsm_person_id.vat', string="VAT")
    acc_number = fields.Char(related='fsm_person_id.acc_number')

    @api.depends('payments_salary','payments_km','payments_diets','payments_advance')
    def _compute_net_salary (self):
        for person in self:
            person.net_salary = (person.payments_salary + person.payments_km + person.payments_diets - person.payments_advance)
