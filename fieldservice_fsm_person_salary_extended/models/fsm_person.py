# © 2023 Solvos Consultoría Informática (<http://www.solvos.es>)
# License AGPL-3 - See http://www.gnu.org/licenses/agpl-3.0.html
from odoo import models, fields, api


class FSMPerson(models.Model):
    _inherit = "fsm.person"
    
    fsm_salary_ids = fields.One2many('fsm.salary', 'fsm_person_id')
        