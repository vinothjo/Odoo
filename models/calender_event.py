# -*- coding: utf-8 -*

from odoo import models, fields, api, _




class CalendarEvent(models.Model):
    _inherit = "calendar.event"
    
    equipments = fields.Many2many('product.product', srting='Equipment', domain=[('is_equipment', '=', True)], required=True)
    
    
    
class HrEmployee(models.Model):
    _inherit = "hr.employee"

    @api.multi
    def _get_event_number(self):
        for employee in self:
            event_add = self.env['calendar.event'].search([('partner_ids', '=', 'hr.employee'),('partner_ids', '=', employee.id)])
            employee.event_number = len(event_add)

    event_number = fields.Integer(compute='_get_event_number', string="Event")
    
    
    @api.multi
    def action_event_number(self):
        equipments = self.action_event_number()
        return {
            'type': 'ir.actions.act_window',
            'res_model': 'calendar.event',
            'view_mode': 'form',
            'res_id': equipments.id,
            'target': 'current',
            'flags': {'form': {'action_buttons': True, 'options': {'mode': 'edit'}}}
        }

