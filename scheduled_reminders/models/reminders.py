# -*- coding: utf-8 -*-

from odoo import models, fields, api
from odoo.exceptions import ValidationError, UserError
from datetime import date, datetime
from dateutil.relativedelta import relativedelta
import smtplib, ssl

class Reminders(models.Model):
    _name = 'reminder.info'
    _description = 'Reminder Information'
    _rec_name = 'description'

    description = fields.Text()
    recipients  = fields.Many2many('email.email')
    list_of_scheduled_reminds = fields.One2many('to.do.list', 'related_field')
    
    time =  fields.Datetime()
    datetime_now = fields.Datetime(default=datetime.now())

    def sending_emails(self):
        for rec in self:
            if rec.time == rec.datetime_now:
                try: 
                    smtp = smtplib.SMTP('smtp.gmail.com', 587) 
                    smtp.starttls() 
                    # or we can use in outgoing mail server in odoo
                    smtp.login("<email>","<password>")
                    message = rec.list_of_scheduled_reminds 
                    smtp.sendmail("<email>",rec.recipients.email,message) 
                    smtp.quit() 
                    print ("Email sent successfully!") 
                except Exception as ex: 
                    print("Something went wrong....",ex)

