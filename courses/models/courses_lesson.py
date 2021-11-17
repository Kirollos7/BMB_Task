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
    room_id = fields.Many2one('course.room.info',string="Room Number")
    
    related_field = fields.Many2one('display.courses')
    
    
    def name_get(self):
        result = []
        for record in self:
            rec_name = f'{record.name} (Room Number: {record.room_id.room_number})' 
            result.append((record.id,rec_name))
        return result