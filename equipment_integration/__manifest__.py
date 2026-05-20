# -*- coding: utf-8 -*-
{
    'name': 'Equipment Integration',
    'version': '16.0.1.0.0',
    'category': 'Maintenance',
    'summary': 'Integrate products with equipment management and invoice tracking',
    'description': """
Equipment Integration Addon
==========================

This addon provides seamless integration between products and equipment:

* Mark products as equipment with boolean field
* Link products to maintenance equipment records
* Create equipment directly from product interface
* Track equipment-related invoices through product connections
* Smart buttons for quick access to related data
* Automated equipment naming from product names
    """,
    'author': 'Equipment Integration Team',
    'website': 'https://github.com/TugayHatil',
    'license': 'LGPL-3',
    'depends': [
        'product',
        'maintenance',
        'account',
    ],
    'data': [
        'security/security.xml',
        'views/product_template_views.xml',
        'views/maintenance_equipment_views.xml',
        'views/equipment_creation_wizard_views.xml',
    ],
    'installable': True,
    'auto_install': False,
    'application': False,
    'sequence': 100,
}
