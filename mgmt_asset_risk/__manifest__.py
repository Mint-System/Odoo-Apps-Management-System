{
    "name": "Mgmt Asset Risk",
    "summary": """
        Connect risk and asset management.
    """,
    "author": "Mint System GmbH",
    "website": "https://www.mint-system.ch/",
    "category": "Management",
    "version": "19.0.1.0.0",
    "license": "AGPL-3",
    "depends": ["mgmt_asset", "mgmt_risk", "mgmt_asset_maintenance"],
    "data": ["views/risk_views.xml", "demo/demo.xml"],
    "installable": True,
    "application": False,
    "auto_install": False,
    "images": ["images/screen.png"],
}
