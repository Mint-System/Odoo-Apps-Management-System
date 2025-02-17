{
    "name": "Mgmt Asset",
    "summary": """
        Manage risk management assets.
    """,
    "author": "Mint System GmbH",
    "website": "https://github.com/OCA/sale-workflow",
    "category": "Management",
    "version": "18.0.1.0.0",
    "license": "AGPL-3",
    "depends": ["mgmt_base", "product", "maintenance"],
    "data": ["security/ir.model.access.csv", "views/asset_views.xml"],
    "demo": ["demo/demo.xml"],
    "installable": True,
    "application": False,
    "auto_install": False,
    "images": ["images/screen.png"],
}
