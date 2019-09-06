{
    "name": "Certification",
    "summary": "sdsadsad",
    'version': '12.0.1.0.0',
    "category":"Certification ",
    "depends": [
        'base','hr','employeeid'
    ],
    "data": [ 'security/ir.model.access.csv',
                'security/certification_security.xml',
                'views/certification_view.xml',
                'views/standard_view.xml',
              'views/res_partner_view.xml',
              'reports/certification_report.xml',
'reports/certification_template_pdf.xml',
'reports/report_certification_pdf.xml'
    ],
    'development_status':'Beta',
    'maintainers':['ceeficent'],
    'demo': ['demo/certification_data.xml','demo/employee_data.xml'],
}
