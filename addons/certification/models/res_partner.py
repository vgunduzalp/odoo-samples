from odoo import models, fields


class ResPartner(models.Model):
    _inherit = 'res.partner'

    certification_ids = fields.One2many(comodel_name='certification', inverse_name='owner_id')
    is_certification_body = fields.Boolean(string='Certification', default='True',
                                           help='Check this box if the contact is a certification entity')

