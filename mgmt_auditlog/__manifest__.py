{
    "name": "Mgmt Auditlog",
    "summary": """
        Setup audit log rules for the mgmt modules.
    """,
    "author": "Mint System GmbH",
    "website": "https://www.mint-system.ch/",
    "category": "Management",
    "version": "18.0.1.0.0",
    "license": "AGPL-3",
    "depends": ["mgmt_audit", "auditlog"],
    "data": ["data/auditlog.xml"],
    "installable": True,
    "application": False,
    "auto_install": False,
    "images": ["images/screen.png"],
}
