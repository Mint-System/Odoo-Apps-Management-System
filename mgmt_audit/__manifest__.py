{
    "name": "Mgmt Audit",
    "summary": """
        Audit your company.
    """,
    "author": "Mint System GmbH, Odoo Community Association (OCA)",
    "website": "https://github.com/OCA/management-system",
    "category": "Management",
    "version": "17.0.1.0.0",
    "license": "AGPL-3",
    "depends": ["mgmt_requirement", "mgmt_risk"],
    "data": ["security/ir.model.access.csv", "views/audit_views.xml", "views/audit_stage_views.xml", "views/statement_views.xml", "views/nonconformity_views.xml", "views/recommendation_views.xml"],
    "demo": ["demo/demo.xml"],
    "installable": True,
    "application": False,
    "auto_install": False,
    "images": ["images/screen.png"],
}
