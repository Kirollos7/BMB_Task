# -*- coding: utf-8 -*-
# from odoo import http


# class ScheduledReminders(http.Controller):
#     @http.route('/scheduled_reminders/scheduled_reminders/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/scheduled_reminders/scheduled_reminders/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('scheduled_reminders.listing', {
#             'root': '/scheduled_reminders/scheduled_reminders',
#             'objects': http.request.env['scheduled_reminders.scheduled_reminders'].search([]),
#         })

#     @http.route('/scheduled_reminders/scheduled_reminders/objects/<model("scheduled_reminders.scheduled_reminders"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('scheduled_reminders.object', {
#             'object': obj
#         })
