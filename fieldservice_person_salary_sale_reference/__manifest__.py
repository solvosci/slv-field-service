# © 2023 Solvos Consultoría Informática (<http://www.solvos.es>)
# License AGPL-3 - See http://www.gnu.org/licenses/agpl-3.0.html
{
    "name": "FieldService Person Salary - Sale Reference link",
    "summary": """
        Adds sale reference to Person Salaty for FSM orders
    """,
    "author": "Solvos",
    "license": "AGPL-3",
    "version": "15.0.1.2.0",
    "category": "Field Service",
    "website": "https://github.com/solvosci/slv-field-service",
    "depends": ["fieldservice_person_salary", "fieldservice_sale_reference"],
    "data": ["views/fsm_order_salary_views.xml"],
    "installable": True,
}
