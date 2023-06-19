# © 2023 Solvos Consultoría Informática (<http://www.solvos.es>)
# License AGPL-3 - See http://www.gnu.org/licenses/agpl-3.0.html
{
    "name": "Fieldservice Equipment Note Sale Reference",
    "summary": """
        Adds sale_reference field in the fsm.order views.
    """,
    "author": "Solvos",
    "license": "AGPL-3",
    "version": "15.0.1.1.0",
    "category": "Field Service",
    "website": "https://github.com/solvosci/slv-field-service",
    "depends": ["fieldservice_equipment_note", "fieldservice_sale_reference"],
    "data": 
        ["views/fsm_equipment_note_views.xml"],
    "installable": True,
}
