from odoo import api, models, fields
from odoo.exceptions import ValidationError, UserError



# This table for create lessons   
class LessonInfo(models.Model):
    _name = 'course.lesson.info'
    _description = 'Lessons Information'
    _inherit = 'mail.thread'
    _order = 'name'
    
    
    name = fields.Char()
    note = fields.Char()
    course_id = fields.Many2one('course.course.info',string="Course Name")
    room_id = fields.Many2one('course.room.info',string="Room Number")
    
    related_field = fields.Many2one('display.courses')
    
    
    def name_get(self):
        result = []
        for record in self:
            rec_name = f'{record.name} (Course Code: {record.course_id.code})' 
            result.append((record.id,rec_name))
        return result