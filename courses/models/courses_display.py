from odoo import api, models, fields
from odoo.exceptions import ValidationError, UserError

# This table 
class CoursesDisplay(models.Model):
   _name = 'display.courses'
   _description = 'Display Courses'
   _inherit = 'mail.thread'
   


   course_id = fields.Many2one('course.course.info', string='Course',)
   instructor_id = fields.Many2one('res.partner', string='Instructor',)
   room = fields.Many2one('course.room.info', string='Room',)
   
   list_of_attendees = fields.Many2many('res.partner', string='Students',) 
   lessons = fields.One2many('course.lesson.info','related_field',string='Lessons',)
 
   @api.constrains('list_of_attendees')
   def validate_name_of_student(self):
      for rec in self:
         size = len(rec.list_of_attendees)
       
         if size > rec.room.capacity_of_room:
            msg = f'Number of Student [{size}] and Capacity of room is [{rec.room.capacity_of_room}] Should Be equal or less than capacity of room.'
            raise ValidationError(msg)
         elif size == rec.room.capacity_of_room:
            ee = f'Number of Student [{size}] and Capacity of room is [{rec.room.capacity_of_room}] NOTE Should Be less than br one of capacity due to Instructor.'
            raise ValidationError(ee)
   
 
   def name_get(self):
      result = []
      for record in self:
         rec_name = f'{record.course_id.name} (Instructor: {record.instructor_id.name})' 
         result.append((record.id,rec_name))
      return result

   @api.onchange('room')
   def onchange_room(self): 
      room_name = self.room.room_name
      obj = self.env['course.lesson.info'].search([('room_id.room_name','=', room_name)])
      self.lessons = obj
      
      
      
   # @api.model
   # def _get_lessons(self, fields):
   #    val = super(CoursesDisplay, self).default_get(fields)
   #    lessons_lines = [(5,0,0)]
   #    lessons = self.env['course.lesson.info'].search([('room_id.room_name','==','room.room_name')])
   #    for rec in lessons:
   #       line = (0,0,{
   #           'name' : rec.id,
   #           'note': rec.id,
   #           'course_id': rec.course_id,
   #          })
   #       lessons_lines.append(line)
   #    val['lessons'] = lessons_lines
   #    return val
      
      
   
    