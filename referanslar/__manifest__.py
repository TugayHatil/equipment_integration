# -*- coding: utf-8 -*-
{
    'name': 'Referanslar',
    'version': '16.0.1.0.0',
    'category': 'Sales/CRM',
    'summary': 'CRM fırsatlarını referans olarak listeleyen uygulama',
    'description': """
Referanslar
===========

CRM fırsatlarını (crm.lead) referans olarak listeleyen uygulama:

* Ana sayfada diğer uygulamaların yanında "Referanslar" uygulaması
* Fırsat, Bayi Adı, Sistem Çözümü, Sektör, Yıl, Gelir ve Aşama sütunları
* crm.lead üzerine yeni "Sektör" alanı
* date_deadline alanından otomatik hesaplanan "Yıl" alanı
* Sektörler için yapılandırma menüsü
    """,
    'author': 'Tugay Hatil',
    'website': 'https://github.com/TugayHatil',
    'license': 'LGPL-3',
    'depends': [
        'crm',
    ],
    'data': [
        'security/ir.model.access.csv',
        'data/referans_sektor_data.xml',
        'views/referans_sektor_views.xml',
        'views/crm_lead_views.xml',
        'views/referans_menu.xml',
    ],
    'installable': True,
    'auto_install': False,
    'application': True,
    'sequence': 100,
}
