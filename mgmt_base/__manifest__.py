{
    "name": "Mgmt Base",
    "summary": """
        Base for the management modules.
    """,
    "author": "Mint System GmbH, Odoo Community Association (OCA)",
    "website": "https://github.com/OCA/management-system",
    "category": "Management",
    "version": "17.0.1.0.0",
    "license": "AGPL-3",
    "depends": ["mgmtsystem"],
    "data": [
        "views/menu.xml",
        "views/res_config_settings.xml",
    ],
    "installable": True,
    "application": False,
    "auto_install": False,
    "images": ["images/screen.png"],
}
