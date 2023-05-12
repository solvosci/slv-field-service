# © 2023 Solvos Consultoría Informática (<http://www.solvos.es>)
# License AGPL-3 - See http://www.gnu.org/licenses/agpl-3.0.html
{
    "name": "Fieldservice Equipment Extended",
    "summary": """
        Add new fields in the fsm order models.
    """,
    "author": "Solvos",
    "license": "AGPL-3",
    "version": "15.0.1.0.0",
    "category": "Field Service",
    "website": "https://github.com/solvosci/slv-field-service",
    "depends": ["fieldservice"],
    "data": 
        [
        "security/ir.model.access.csv",
        "reports/fsm_order_template.xml",
        "views/fsm_order_views.xml",
        ],
    "installable": True,
}
