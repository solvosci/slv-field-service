# © 2023 Solvos Consultoría Informática (<http://www.solvos.es>)
# License AGPL-3 - See http://www.gnu.org/licenses/agpl-3.0.html
from odoo import models, fields


class FSMEquipmentNote(models.Model):
    _name = "fsm.equipment.note"

    fsm_order_id = fields.Many2one('fsm.order')
    sequence = fields.Integer()
    fms_equipment_id = fields.Many2one('fsm.equipment', required=True)
    observation = fields.Char(required=True)
