from odoo import http
from odoo.http import request
import json
from odoo.addons.website_sale.controllers.main import WebsiteSale


class Courses(http.Controller):
    @http.route('/courses/', type="http", auth='public')
    def get_courses(self, **kw):
        courses_object = request.env['display.courses'].search([])
        courses = []
        for rec in courses_object:
            vals = {
                'Course name': rec.course_id.name,
                'Instructor name': rec.instructor_id.name,
                'Room name': rec.room.room_name,
            }
            courses.append(vals)
        data = {
            'status': "200",
            'message': "success",
            'courses': courses,
        }
        return json.dumps(data, indent=4,)
    
