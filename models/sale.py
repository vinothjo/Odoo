# -*- coding: utf-8 -*

from odoo import models, fields, api



class SalesBooking(models.Model):
    _inherit = 'sale.order'
    
    is_booking = fields.Boolean(string="Is Booking")
    team_id = fields.Many2one('team.book', string="Team")
    leader_id = fields.Many2one('hr.employee', related='team_id.leader_id', string='Leader')
    booking_start = fields.Date(string="Booking Start")
    booking_end = fields.Date(string="Booking End")



