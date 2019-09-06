import odoo.tests.common as common


class TestCertification(common.TransactionCase):

   def setUp(self):
       super(TestCertification, self).setUp()
       self.res_partner = self.env['res.partner']
       self.partner = self.res_partner.create({
           'name': "test1",
           'email': "test@test.com"})

   def test_certification(self):
       certification = self.env['certification'].create({
           'number': 'AAA',
           'date': '2025-12-31'})
       self.assertEqual(certification.expiry_status, 'available')