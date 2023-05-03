# © 2023 Solvos Consultoría Informática (<http://www.solvos.es>)
# License AGPL-3 - See http://www.gnu.org/licenses/agpl-3.0.html
{
    "name": "FieldService Person Salary Skill",
    "summary": """
        Adds skills to Person Salary for FSM order.
    """,
    "author": "Solvos",
    "license": "AGPL-3",
    "version": "15.0.1.1.0",
    "category": "Field Service",
    "website": "https://github.com/solvosci/slv-field-service",
    "depends": ["fieldservice_person_salary", "fieldservice_skill"],
    "data": ["views/fsm_order_salary_views.xml"],
    "installable": True,
}
