from psycopg2.extensions import AsIs
from odoo import tools
from odoo import api, fields, models


class CertificationReport2(models.Model):
    _name = "certification.report"
    _description = "Certification Report 2"
    _auto = False

    entity_id = fields.Many2one('res.partner', readonly=True)
    certification_count = fields.Integer(readonly=True)
    standard_id = fields.Many2one('certification.standard')
    expiry_status = fields.Selection([
        ('expired', "Expired"),
        ('available', "Available")
    ], readonly=True)


    def _select(self):
       select_str = """
          SELECT
                  rp.id AS id,
                  c.entity_id AS entity_id,
                  cs.id AS standard_id,
                  c.expiry_status AS expiry_status,
                  count(c.id) AS certification_count
      """
       return select_str

    def _from(self):
       from_str = """
          res_partner AS rp
          JOIN certification AS c
          ON c.entity_id = rp.id
          JOIN certification_standard AS cs
          ON cs.id = c.standard_id
          """
       return from_str

    def _where(self):
      where_str = """rp.is_certification_body is True"""
      return where_str

    def _group_by(self):
       group_by_str = """
          GROUP BY
          rp.id,
          c.entity_id,
          cs.id,
          c.expiry_status
      """
       return group_by_str


    @api.model_cr
    def init(self):
        tools.drop_view_if_exists(self.env.cr, self._table)
        self.env.cr.execute(
            """
            CREATE or REPLACE VIEW %s as (%s
            FROM ( %s ) WHERE ( %s )
            %s)""",
            (AsIs(self._table), AsIs(self._select()),
             AsIs(self._from()), AsIs(self._where()),
             AsIs(self._group_by())),
        )
