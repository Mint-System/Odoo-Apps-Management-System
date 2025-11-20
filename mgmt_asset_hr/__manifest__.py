# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).
{
    "name": "Mgmt Asset HR",
    "summary": """
        Add owner to employee.
    """,
    "author": "Mint System GmbH",
    "website": "https://www.mint-system.ch/",
    "category": "Repository",
    "development_status": "Production/Stable",
    "version": "18.0.1.0.0",
    "license": "AGPL-3",
    "depends": ["mgmt_asset", "hr"],
    "data": ["views/hr_employee_views.xml"],
    "installable": True,
    "application": False,
    "auto_install": False,
    "images": ["images/screen.png"],
}
