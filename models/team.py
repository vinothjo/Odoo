# -*- coding: utf-8 -*

from odoo import models, fields, api, _

class TeamBook(models.Model):
    _name = 'team.book'
    
    name = fields.Char(string='Name', required=True,)
    employee_ids = fields.Many2many('hr.employee', string='Team Members')
    leader_id = fields.Many2one('hr.employee', string='Leader',required=True,)
    equipment_ids = fields.Many2many('product.product', string='Equipment', domain=[('is_equipment', '=', True)], required=True)
    
    
