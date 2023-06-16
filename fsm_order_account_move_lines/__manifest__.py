# © 2023 Solvos Consultoría Informática (<http://www.solvos.es>)
# License AGPL-3 - See http://www.gnu.org/licenses/agpl-3.0.html
{
    "name": "Fildservice Order Account Move Lines",
    "summary": """
        Adds fsm_order_id field in the account_move_line views.
    """,
    "author": "Solvos",
    "license": "AGPL-3",
    "version": "15.0.1.0.0",
    "category": "Field Service",
    "website": "https://github.com/solvosci/slv-field-service",
    "depends": ["fieldservice", "account", "fieldservice_sale"],
    "data": [
        "views/account_move_line_views.xml",
        "views/account_move_views.xml",
        "views/fsm_order_menu.xml",
        "views/fsm_order_views.xml",
        ],
    "installable": True,
}
