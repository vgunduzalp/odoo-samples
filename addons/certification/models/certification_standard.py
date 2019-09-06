from odoo import models,fields,api

class CertificationStandard(models.Model):
    _name='certification.standard'
    _description='Certification Types'

    name= fields.Char()
    description=fields.Text()