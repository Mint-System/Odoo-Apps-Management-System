{
    "name": "Mgmt Audit Project",
    "summary": """
        Create tasks for nonconformities and recommendations.
    """,
    "author": "Mint System GmbH",
    "website": "https://www.mint-system.ch/",
    "category": "Management",
    "version": "19.0.1.0.0",
    "license": "AGPL-3",
    "depends": ["mgmt_audit", "project"],
    "data": [
        "data/data.xml",
        "views/nonconformity_views.xml",
        "views/recommendation_views.xml",
        "views/project_task_views.xml",
    ],
    "demo": [
        "demo/demo.xml",
    ],
    "installable": True,
    "application": False,
    "auto_install": False,
    "images": ["images/screen.png"],
}
