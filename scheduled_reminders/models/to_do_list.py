# -*- coding: utf-8 -*-

from odoo import models, fields, api
from odoo.exceptions import ValidationError, UserError


class ListOfScheduledReminds(models.Model):
    _name = 'to.do.list'
    _description = 'To Do List'

    name = fields.Char(required=True)
    note = fields.Char()
    
    related_field = fields.Many2one('reminder.info',)