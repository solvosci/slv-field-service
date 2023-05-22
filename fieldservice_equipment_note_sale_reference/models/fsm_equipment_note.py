# © 2023 Solvos Consultoría Informática (<http://www.solvos.es>)
# License AGPL-3 - See http://www.gnu.org/licenses/agpl-3.0.html
from odoo import models, fields


class FSMEquipmentNote(models.Model):
    _inherit = "fsm.equipment.note"

    sale_reference = fields.Char(
        related="fsm_order_id.sale_reference", 
        string="Reference", store= True)
