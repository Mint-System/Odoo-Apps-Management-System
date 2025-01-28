{
    "name": "Mgmt Auditlog",
    "summary": """
        Setup audit log rules for the mgmt modules.
    """,
    "author": "Mint System GmbH",
    "website": "https://github.com/OCA/management-system",
    "category": "Management",
    "version": "17.0.1.0.0",
    "license": "AGPL-3",
    "depends": ["mgmt_audit", "auditlog"],
    "data": ["data/auditlog.xml"],
    "installable": True,
    "application": False,
    "auto_install": False,
    "images": ["images/screen.png"],
}
