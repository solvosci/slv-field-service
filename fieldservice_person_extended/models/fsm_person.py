# © 2023 Solvos Consultoría Informática (<http://www.solvos.es>)
# License AGPL-3 - See http://www.gnu.org/licenses/agpl-3.0.html

from odoo import models, fields


class FSMPerson(models.Model):
    _inherit = "fsm.person"
    
    vat = fields.Char(string="VAT")
    acc_number = fields.Char()
