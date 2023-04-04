# © 2023 Solvos Consultoría Informática (<http://www.solvos.es>)
# License AGPL-3 - See http://www.gnu.org/licenses/agpl-3.0.html
from odoo import models, fields, api


class FSMSalary(models.Model):
    _name = "fsm.salary"
    
    fsm_order_id = fields.Many2one('fsm.order', required=True)
    sequence = fields.Integer()
    fsm_person_id = fields.Many2one('fsm.person', required=True)
    vehicle = fields.Boolean()
    payments_salary = fields.Monetary(string='Salary')
    payments_km = fields.Monetary(string='Km')
    payments_diets = fields.Monetary(string='Diets')
    payments_advance = fields.Monetary(string='Advance')
    net_salary = fields.Monetary(currency_field='currency_id',
            compute='_compute_net_salary',
            string='Net Salary', store=True)
    currency_id = fields.Many2one('res.currency', 'Currency', required=True,
            default=lambda self: self.env.company.currency_id.id)

    @api.depends('payments_salary','payments_km','payments_diets','payments_advance')
    def _compute_net_salary (self):
        for person in self:
            person.net_salary = (person.payments_salary + person.payments_km + person.payments_diets - person.payments_advance)
