# -*- coding: utf-8 -*-

from odoo import models, fields, api
from odoo.exceptions import ValidationError, UserError
import re


class RecipientsByEmail(models.Model):
    _name = 'email.email'
    _description = 'Emails'
    _rec_name = 'email'
    
    email = fields.Char(required=True)

    _sql_constraints = [
        ('unique_email', 'UNIQUE(email)', 'This Email Already Exit, [Please Check And Try Again]'),
    ]

    @api.constrains('email')
    def validate_email(self):
        for obj in self:
            if re.match("^.+\\@(\\[?)[a-zA-Z0-9\\-\\.]+\\.([a-zA-Z]{2,3}|[0-9]{1,3})(\\]?)$", obj.email) == None:
                raise ValidationError("Please Provide Valid Email Address: %s" % obj.email)
        return True


   