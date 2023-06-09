# © 2023 Solvos Consultoría Informática (<http://www.solvos.es>)
# License AGPL-3 - See http://www.gnu.org/licenses/agpl-3.0.html

from odoo import fields, models


class FSMTemplate(models.Model):
    _inherit = "fsm.template"

    collaborator_instructions = fields.Html()
