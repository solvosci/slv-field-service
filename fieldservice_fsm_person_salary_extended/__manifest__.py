# © 2023 Solvos Consultoría Informática (<http://www.solvos.es>)
# License AGPL-3 - See http://www.gnu.org/licenses/agpl-3.0.html
{
    "name": "FieldService FSM Person Salary Extended",
    "summary": """
        Adds salary fields in fsm.salary model
    """,
    "author": "Solvos",
    "license": "AGPL-3",
    "version": "15.0.1.0.0",
    "category": "Field Service",
    "website": "https://github.com/solvosci/slv-field-service",
    "depends": ["fieldservice"],
    "data": [
        "security/ir.model.access.csv",
        "views/fsm_order_views.xml",
        "views/fsm_salary_views.xml",
        "views/fsm_salary_menu.xml",
            ],
    "installable": True,
}
