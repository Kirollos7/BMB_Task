from odoo import api, models, fields
from odoo.exceptions import ValidationError, UserError

class Person(models.Model):
    _inherit = 'res.partner'
    
    CHOICES = [
        ('instructor','Instructor'),
        ('student','Student'),
    ]
    instructor_or_student  = fields.Selection(CHOICES, required=True, default="instructor")
    courses_ids = fields.Many2many('course.course.info', string="Courses")
    