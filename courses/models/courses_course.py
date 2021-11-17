from odoo import api, models, fields
from odoo.exceptions import ValidationError, UserError


# This table for (Core Table) for create courses

class CourseInfo(models.Model):
    _name = 'course.course.info'
    _description = 'Courses Information'
    _inherit = 'mail.thread'
    _order = 'code'
    
    name = fields.Char(index=True)
    code = fields.Char(help="EX: CS240", required=True)
    number_of_hours = fields.Float()
    content_as_pdf  = fields.Binary(string="Upload Content")
    note = fields.Html()
   
    _sql_constraints = [
        ('unique_code' , 'UNIQUE(code)' , 'This Code is Already Exit, [Please Check And Try Again].'),
    ]
    
    @api.constrains('number_of_hours')
    def validate_hours(self):
        for rec in self:
            if rec.number_of_hours <= 0:
                msg = f'Number of hours [{rec.number_of_hours}] Should Be Positive Number'
                raise ValidationError(msg)
    