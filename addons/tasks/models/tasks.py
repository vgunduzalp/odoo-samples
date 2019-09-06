from odoo import models,fields,api
from datetime import timedelta


class Tasks(models.Model):
    _name='tasks'
    _description='Task Management'

    title = fields.Char(string='Title', required=True)
    description = fields.Text(string='Description')
    start_date= fields.Date(string='Satrt Date')
    end_date = fields.Date(string='End Date')
    deadline = fields.Date(string='Deadline',required=True)
    assigned_to = fields.Many2one("hr.employee",required=True)

    effort = fields.Integer('Efort')
    status = fields.Selection([
        ('todo', "ToDo"),
        ('in_progress', "In Progress"),
        ('removed', "Removed"),
        ('done', "Done")
    ],required=True)

    isExpired = fields.Boolean(string = "Durum", readonly=True, compute='_compute_expiry_days')

"""
    @api.multi
    def _compute_expiry_days(self):
        self.ensure_one()
        if True:
            self.isExpired = True
        else:
            self.isExpired = False

"""