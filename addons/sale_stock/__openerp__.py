# -*- coding: utf-8 -*-
##############################################################################
#
#    OpenERP, Open Source Management Solution
#    Copyright (C) 2004-2010 Tiny SPRL (<http://tiny.be>).
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################

{
    'name': 'Sales and Warehouse Management',
    'version': '1.0',
    'category': 'Hidden',
    'summary': 'Quotation, Sale Orders, Delivery & Invoicing Control',
    'description': """
Manage sales quotations and orders
==================================

This application allows you to manage your sales goals in an effective and efficient manner by keeping track of all sales orders and history.

It handles the full sales workflow:

* **Quotation** -> **Sales order** -> **Invoice**

Preferences
-----------
* Shipping: Choice of delivery at once or partial delivery
* Invoicing: choose how invoices will be paid
* Incoterms: International Commercial terms

You can choose flexible invoicing methods:

* *On Demand*: Invoices are created manually from Sales Orders when needed
* *On Delivery Order*: Invoices are generated from picking (delivery)
* *Before Delivery*: A Draft invoice is created and must be paid before delivery


The Dashboard for the Sales Manager will include
------------------------------------------------
* My Quotations
* Monthly Turnover (Graph)
""",
    'author': 'OpenERP SA',
    'website': 'http://www.openerp.com',
    'images': ['images/deliveries_to_invoice.jpeg'],
    'depends': ['sale', 'stock', 'procurement'],
    'init_xml': [],
    'update_xml': ['security/sale_stock_security.xml',
                   'security/ir.model.access.csv',
                   'company_view.xml',
                   'sale_stock_view.xml',
                   'sale_stock_workflow.xml',
                   'res_config_view.xml',
                   'report/sale_report_view.xml',
                   'process/sale_stock_process.xml',
                   ],
   'data': ['sale_stock_data.xml'],
   'demo_xml': ['sale_stock_demo.xml'],
    'test': ['test/cancel_order_sale_stock.yml',
             'test/picking_order_policy.yml',
             'test/prepaid_order_policy.yml',
             ],
    'installable': True,
    'auto_install': True,
    
}
# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
