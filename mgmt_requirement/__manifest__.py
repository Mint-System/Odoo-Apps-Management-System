{
    "name": "Mgmt Requirement",
    "summary": """
        Manage organisational requirements.
    """,
    "author": "Mint System GmbH, Odoo Community Association (OCA)",
    "website": "https://github.com/OCA/management-system",
    "category": "Management",
    "version": "17.0.1.0.0",
    "license": "AGPL-3",
    "depends": ["mgmt_base"],
    "data": [
        "security/ir.model.access.csv",
        "views/requirement_views.xml",
        "views/paragraph_views.xml",
        "views/document_views.xml",
        "views/tag_views.xml",
    ],
    "demo": ["demo/demo.xml"],
    "installable": True,
    "application": False,
    "auto_install": False,
    "images": ["images/screen.png"],
}
