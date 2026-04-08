# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).
{
    "name": "Mgmt Asset Maintenance",
    "summary": """
        Add owner to maintenance equipment.
    """,
    "author": "Mint System GmbH",
    "website": "https://www.mint-system.ch/",
    "category": "Repository",
    "development_status": "Production/Stable",
    "version": "19.0.1.0.0",
    "license": "AGPL-3",
    "depends": ["mgmt_asset", "maintenance"],
    "data": [
        "views/maintenance_equipment_views.xml",
        "views/maintenance_equipment_category_views.xml",
    ],
    "demo": [
        "demo/demo.xml",
    ],
    "installable": True,
    "application": False,
    "auto_install": False,
    "images": ["images/screen.png"],
}
