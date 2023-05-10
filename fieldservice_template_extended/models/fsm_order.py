# © 2023 Solvos Consultoría Informática (<http://www.solvos.es>)
# License AGPL-3 - See http://www.gnu.org/licenses/agpl-3.0.html

from odoo import fields, models


class FSMOrder(models.Model):
    _inherit = "fsm.order"

    collaborator_todo = fields.Html()

    def copy_notes(self):
        action = super(FSMOrder, self).copy_notes()
        if self.template_id:
            self.collaborator_todo = self.template_id.collaborator_instructions
        return action
