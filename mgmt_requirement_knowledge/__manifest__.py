# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).
{
    "name": "Mgmt Requirement Knowledge",
    "summary": """
        Links Requirement to Documentation.
    """,
    "author": "Mint System GmbH",
    "website": "https://www.mint-system.ch/",
    "category": "Repository",
    "development_status": "Production/Stable",
    "version": "18.0.1.0.0",
    "license": "AGPL-3",
    "depends": ["base", "mgmt_requirement", "knowledge"],
    "data": [
        "security/ir.model.access.csv",
        "views/paragraph_views.xml",
        "views/knowledge_views.xml",
    ],
    "installable": True,
    "application": False,
    "auto_install": False,
    "images": ["images/screen.png"],
}
