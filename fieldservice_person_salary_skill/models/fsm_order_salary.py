# © 2023 Solvos Consultoría Informática (<http://www.solvos.es>)
# License AGPL-3 - See http://www.gnu.org/licenses/agpl-3.0.html
from odoo import models, fields


class FSMOrderSalary(models.Model):
    _inherit = "fsm.order.salary"

    person_skill_ids = fields.One2many(
        related="fsm_person_id.skill_ids"
    )
