{
    "name": "Mgmt Audit",
    "summary": """
        Audit your company.
    """,
    "author": "Mint System GmbH",
    "website": "https://www.mint-system.ch/",
    "category": "Management",
    "version": "18.0.1.0.0",
    "license": "AGPL-3",
    "depends": ["mgmt_requirement", "mgmt_risk"],
    "data": [
        "security/ir.model.access.csv",
        "data/data.xml",
        "views/audit_views.xml",
        "views/audit_stage_views.xml",
        "views/statement_views.xml",
        "views/nonconformity_views.xml",
        "views/recommendation_views.xml",
        "views/risk_views.xml",
    ],
    "demo": ["demo/demo.xml"],
    "installable": True,
    "application": False,
    "auto_install": False,
    "images": ["images/screen.png"],
}
