from psycopg2.extensions import AsIs
from odoo import tools
from odoo import api, fields, models


class TasksReport(models.Model):
    _name = "tasks.report"
    _description = "Task Report"
    _auto = False

    assigned_to = fields.Many2one("hr.employee",required=True)
    task_count = fields.Integer(readonly=True)
    #standard_id = fields.Many2one('certification.standard')
    status = fields.Selection([
        ('todo', "ToDo"),
        ('in_progress', "In Progress"),
        ('removed', "Removed"),
        ('done', "Done")
    ], required=True)


    def _select(self):
       select_str = """
          SELECT
                    h.id as id,
                  h.id AS assigned_to,
                  t.status AS status,
                  count(t.id) AS task_count
      """
       return select_str

    def _from(self):
       from_str = """
          tasks AS t JOIN hr_employee AS h ON t.assigned_to = h.id
          """
       return from_str

    def _where(self):
      where_str = """1 = 1"""
      return where_str

    def _group_by(self):
       group_by_str = """
          GROUP BY
          h.id,
          t.status
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
             AsIs(self._from()),
             AsIs(self._where()),
             AsIs(self._group_by())),
        )
