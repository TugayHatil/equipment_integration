# -*- coding: utf-8 -*-
from odoo import fields, models


class ReferansSektor(models.Model):
    _name = 'referans.sektor'
    _description = 'Referans Sektörü'
    _order = 'name'

    name = fields.Char(string='Sektör', required=True, translate=True)
    color = fields.Integer(string='Renk')
    active = fields.Boolean(string='Aktif', default=True)
