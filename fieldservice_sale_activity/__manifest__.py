# © 2023 Solvos Consultoría Informática (<http://www.solvos.es>)
# License AGPL-3 - See http://www.gnu.org/licenses/agpl-3.0.html
{
    "name": "Fieldservice Sale Activities",
    "summary": """
        Adds improvement that when confirming a sales order all the activities of the product templates are added to the fsm.order
    """,
    "author": "Solvos",
    "license": "AGPL-3",
    "version": "15.0.1.0.0",
    "category": "Field Service",
    "website": "https://github.com/solvosci/slv-field-service",
    "depends": [
        "fieldservice_sale",
        "fieldservice_activity",
    ],
    "data": [],
    'installable': True,
}
