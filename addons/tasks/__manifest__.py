{
    "name": "tasks",
    "summary": "Task Management",
    'version': '1.0.1',
    "category":"tasks ",
    "depends": [
        'base','hr'
    ],
    "data": [ 'security/ir.model.access.csv',
                'security/tasks_security.xml',
                'views/tasks_view.xml',
                'reports/employee_tasks_report.xml',
                'reports/tasks_status_report.xml'
    ],
    'development_status':'Beta'
}
