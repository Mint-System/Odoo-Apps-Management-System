{
    "name": "Mgmt Risk",
    "summary": """
        Manage risks for ISO27001.
    """,
    "author": "Mint System GmbH",
    "website": "https://github.com/OCA/sale-workflow",
    "category": "Management",
    "version": "18.0.1.0.0",
    "license": "AGPL-3",
    "depends": ["mgmt_base", "hr", "mail"],
    "data": [
        "security/ir.model.access.csv",
        "data/data.xml",
        "views/risk_views.xml",
        "views/risk_stage_views.xml",
        "views/hazard_views.xml",
        "views/severity_views.xml",
        "views/probability_views.xml",
        "views/risk_combination_views.xml",
        "views/res_config_settings.xml",
    ],
    "demo": ["demo/demo.xml"],
    "assets": {
        "web.assets_backend": [
            "mgmt_risk/static/src/css/styles.css",
        ],
    },
    "installable": True,
    "application": False,
    "auto_install": False,
    "images": ["images/screen.png"],
}
