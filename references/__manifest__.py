# -*- coding: utf-8 -*-
{
    'name': "Referanslar",

    'summary': "CRM fırsatlarını referans olarak listeleyen uygulama",

    'description': """CRM fırsatlarının (crm.lead) referans listesi için Referanslar.

Ana sayfada diğer uygulamaların yanında Referanslar uygulaması ekler.
Liste görünümünde Fırsat, Bayi Adı, Sistem Çözümü (etiketler), Sektör,
Yıl, Gelir ve Aşama sütunları gösterilir; arama çubuğunda aynı alanlar
ve Kazanılan filtresi ile Sektör / Yıl / Aşama / Bayi Adı gruplamaları
bulunur.

crm.lead modeline Sektör alanı eklenir; Kontaklar uygulamasındaki
mevcut sektör modeli (res.partner.industry) kullanılır ve fırsat
formunda Telefon alanının hemen altında yer alır. Yıl alanı, fırsatın
Beklenen Kapanış (date_deadline) tarihinden otomatik hesaplanır ve
saklanır.

CRM > Satış altında, Müşteriler'in hemen altında Sektörler menüsü
eklenir; Kontaklar > Yapılandırma'dakiyle aynı sektör listesini açar.

Liste veya form görünümünden seçili kayıtlar için Yazdır menüsünden
şirket logosu ve adres bilgilerini içeren Referanslar PDF çıktısı
alınabilir.""",

    'author': "Projet Solutions",
    'website': "https://projet.solutions",

    'category': 'Sales/CRM',
    'version': '16.0.1.0.0',

    'depends': [
        'crm',
    ],

    'data': [
        'views/crm_lead_views.xml',
        'views/referans_menu.xml',
        'report/referanslar_report.xml',
    ],
    'license': 'LGPL-3',
    'installable': True,
    'auto_install': False,
    'application': True,
}
