{
    "name": "Mgmt Risk",
    "summary": """
        Manage risks for ISO27001.
    """,
    "author": "Mint System GmbH, Odoo Community Association (OCA)",
    "website": "https://github.com/OCA/management-system",
    "category": "Management",
    "version": "17.0.1.0.0",
    "license": "AGPL-3",
    "depends": ["mgmt_base", "hr"],
    "data": [
        "security/ir.model.access.csv",
        "views/risk_views.xml",
        "views/hazard_views.xml",
        "views/severity_views.xml",
        "views/probability_views.xml",
        "views/risk_combination_views.xml",
    ],
    "demo": ["demo/demo.xml"],
    "installable": True,
    "application": False,
    "auto_install": False,
    "images": ["images/screen.png"],
}
