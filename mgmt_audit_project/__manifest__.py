{
    "name": "Mgmt Audit Project",
    "summary": """
        Create tasks for nonconformities and recommendations.
    """,
    "author": "Mint System GmbH, Odoo Community Association (OCA)",
    "website": "https://github.com/OCA/management-system",
    "category": "Management",
    "version": "17.0.1.0.0",
    "license": "AGPL-3",
    "depends": ["mgmt_audit", "project"],
    "data": [
        "views/nonconformity_views.xml",
        "views/recommendation_views.xml",
        "views/project_task_views.xml",
    ],
    "demo": ["demo/demo.xml"],
    "installable": True,
    "application": False,
    "auto_install": False,
    "images": ["images/screen.png"],
}
