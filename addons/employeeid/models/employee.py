from odoo import models, fields, api



class EmployeeInfo(models.Model):

    _name = 'employee.info'
    _description = 'EmployeeTest'

    name = fields.Many2one("hr.employee")
    identification_number = fields.Char()
    type = fields.Selection([
        ('passport_id', 'Passport'),
        ('card_id', 'Tc Kimlik'),
        ('driving_license', 'Surucu Belgesi')
    ])
