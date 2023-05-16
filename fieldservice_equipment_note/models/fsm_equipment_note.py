# © 2023 Solvos Consultoría Informática (<http://www.solvos.es>)
# License AGPL-3 - See http://www.gnu.org/licenses/agpl-3.0.html
from odoo import models, fields


class FSMEquipmentNote(models.Model):
    _name = "fsm.equipment.note"
    _description = "Equipment notes on FSM Order"

    fsm_order_id = fields.Many2one('fsm.order')
    sequence = fields.Integer()
    fsm_equipment_id = fields.Many2one(
        'fsm.equipment', 
        string="Equipment",
        required=True)
    note = fields.Char(required=True)
    scheduled_date_start = fields.Datetime(
        related='fsm_order_id.scheduled_date_start',
        store=True)
#     sale_reference = fields.Char(
#             related="fsm_order_id.sale_reference", 
#             string="Reference", store= True)
