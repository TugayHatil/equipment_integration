# -*- coding: utf-8 -*-
# Copyright © 2026 Projet (https://bulutkobi.io)
# Part of Projet License. See LICENSE file for full copyright and licensing details.

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
* crm.lead üzerine "Sektör" alanı (res.partner.industry, Kontaklar/Sektörler)
* date_deadline alanından otomatik hesaplanan "Yıl" alanı
* CRM > Satış > Müşteriler altında Sektörler menüsü
* Seçili kayıtlar için PDF yazdırma çıktısı
    """,
    'author': 'Projet',
    'website': 'https://bulutkobi.io',
    'license': 'LGPL-3',
    'depends': [
        'crm',
    ],
    'data': [
        'views/crm_lead_views.xml',
        'views/referans_menu.xml',
        'report/referanslar_report.xml',
    ],
    'installable': True,
    'auto_install': False,
    'application': True,
    'sequence': 100,
    'images': ['static/description/icon.png'],
}
