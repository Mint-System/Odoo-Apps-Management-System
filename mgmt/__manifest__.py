{
    'name': "Management (Requirements, Compliance, Audits)",
    'summary': """Various functionalities in the context of management""",
    'author': "Mint System GmbH",
    'website': "https://www.mint_system.ch",
    'license': "AGPL-3",
    'category': 'Services/Management',
    'version': "16.0.0.0.4",
    'depends': ['base', 'mail'],  
    #'depends': ['base', 'mail', 'hr'],    
    'data': [
        'views/mgmt.xml',
        'views/mgmt_regulations.xml',
        'views/mgmt_audit.xml',
        'views/mgmt_requirement.xml',
        'views/mgmt_compliance.xml',
        'views/mgmt_paragraph.xml',  
        'views/mgmt_document.xml',
        'views/mgmt_configuration.xml',
        'views/mgmt_nonconformity.xml',
        'views/mgmt_compliancestatement.xml',
        'views/mgmt_docustructure.xml',              
        'security/mgmt_security.xml',
        'security/ir.model.access.csv', 
        'reports/audit_report.xml',
        'reports/audit_program.xml',
        'reports/paragraph.xml', 
        'reports/custom_layout.xml',
        'data/mgmt.audit.type.csv',
        'data/mgmt.audit.category.csv',
        'data/ir.actions.server.csv',
        'data/ir.filters.csv',  
        'demo/res.partner.csv',   
        'demo/mgmt.document.csv',
        'demo/mgmt.docustructure.csv',
        'demo/mgmt.paragraph.csv',
        'demo/mgmt.audit.csv',
        'demo/mgmt.requirement.csv',
        'demo/mgmt.compliancestatement.csv',
        'demo/mgmt.nonconformity.csv',
        'demo/base.document.layout.csv',
        'demo/report.paperformat.csv',
        'demo/res.lang.csv',
        'demo/res.company.csv',
    ], 
    "installable": True,
    "application": True,
    "images": ["images/screen.png"],
}