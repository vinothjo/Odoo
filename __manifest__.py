# -*- coding: utf-8 -*-
{
    'name' : 'Booking Service',
    'version': '1.0',
    'author': 'Vinoth',
    'category' : 'Sale',

    'description': ''' 
Booking Service
  ''',
    'depends':['sale','stock'],
    'data' : [
        'views/sale_views.xml',
        'views/work_order_view.xml',
        'views/team_view.xml',
        'views/calender_event_view.xml',
        'views/product_view.xml',
              ],
    'installable':True,
    'auto_install':False
}

