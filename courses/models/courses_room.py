from odoo import api, models, fields
from odoo.exceptions import ValidationError, UserError


# This table for register data of rooms like a room number, room location
  
class RoomInfo(models.Model):
    _name = 'course.room.info'
    _description = 'Room Information'
    _inherit = 'mail.thread'
    _order = 'room_number'
    
    room_name = fields.Char(index=True,)
    room_number = fields.Char(required=True,  copy=False)
    note = fields.Text()
    location = fields.Char(help="Building NO.10 Floor NO.5")
    capacity_of_room = fields.Integer()
    
    color = fields.Integer()
    
    _sql_constraints = [
        ('unique_room_number' , 'unique (room_number)' , 'This Room Number is Already Exit, [Please Check And Try Again].'),
    ]

    def name_get(self):
        result = []
        for record in self:
            rec_name = f'{record.room_name} (NO.{record.room_number})' 
            result.append((record.id,rec_name))
        return result
    
    
    @api.constrains('capacity_of_room')
    def validate_capacity_of_room(self):
        for rec in self:
            if rec.capacity_of_room <= 0:
                msg = f'Capacity of Room [{rec.capacity_of_room}] Should Be Positive Number'
                raise ValidationError(msg)
    