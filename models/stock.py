# -*- coding: utf-8 -*

from odoo import models, fields, api

class StockWorkOrder(models.Model):
    _inherit = 'stock.picking'
    
    is_booking = fields.Boolean(string="Is booking")
    team_id = fields.Many2one('team.book', string="Team")
    equipments = fields.Many2one('product.product', string="Equipments")
    leader_id = fields.Many2one('hr.employee', related='team_id.leader_id', string='Leader')
    employee_ids = fields.Many2many('hr.employee', string='Team Members')
    schedule_start = fields.Date(string="Schedule Start")
    schedule_end = fields.Date(string="Schedule End")
    actual_start = fields.Date(string="Actual Start")
    actual_end = fields.Date(string="Actual End")
    
class ProductProduct(models.Model):
    _inherit = 'product.template'
    
    is_equipment = fields.Boolean(string="Is an equipment")
    
    
    
