# © 2023 Solvos Consultoría Informática (<http://www.solvos.es>)
# License AGPL-3 - See http://www.gnu.org/licenses/agpl-3.0.html
{
    "name": "Fieldservice Sale Reference",
    "summary": """
        Adds new field "sale_reference" to fsm.order that autofill with the sales order
    """,
    "author": "Solvos",
    "license": "LGPL-3",
    "version": "15.0.1.0.0",
    "category": "Field Service",
    "website": "https://github.com/solvosci/slv-field-service",
    "depends": [
        "fieldservice_sale",
    ],
    "data": [
        "views/fsm_order_views.xml"
    ],
    'installable': True,
}
