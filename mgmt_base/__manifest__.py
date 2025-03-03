{
    "name": "Mgmt Base",
    "summary": """
        Base for the management modules.
    """,
    "author": "Mint System GmbH",
    "website": "https://www.mint-system.ch/",
    "category": "Management",
    "version": "18.0.1.0.0",
    "license": "AGPL-3",
    "depends": ["base"],
    "data": [
        "security/security.xml",
        "security/ir.model.access.csv",
        "views/system.xml",
        "views/menu.xml",
        "views/res_config_settings.xml",
    ],
    "installable": True,
    "application": False,
    "auto_install": False,
    "images": ["images/screen.png"],
}
