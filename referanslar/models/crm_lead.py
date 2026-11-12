# -*- coding: utf-8 -*-
from odoo import api, fields, models


class CrmLead(models.Model):
    _inherit = 'crm.lead'

    sektor_id = fields.Many2one(
        'res.partner.industry',
        string='Sektör',
        ondelete='set null',
        tracking=True,
    )
    referans_yil = fields.Char(
        string='Yıl',
        compute='_compute_referans_yil',
        store=True,
    )

    @api.depends('date_deadline')
    def _compute_referans_yil(self):
        for lead in self:
            lead.referans_yil = str(lead.date_deadline.year) if lead.date_deadline else False
