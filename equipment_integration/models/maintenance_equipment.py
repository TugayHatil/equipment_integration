# -*- coding: utf-8 -*-
from odoo import models, fields, api


class MaintenanceEquipment(models.Model):
    _inherit = 'maintenance.equipment'

    product_ids = fields.One2many(
        'product.template',
        'equipment_id',
        string='Linked Products'
    )
    product_count = fields.Integer(
        string='Product Count',
        compute='_compute_product_count',
        store=True
    )
    invoice_count = fields.Integer(
        string='Invoice Count',
        compute='_compute_invoice_count',
        store=False
    )

    @api.depends('product_ids')
    def _compute_product_count(self):
        """Count linked products"""
        for equipment in self:
            equipment.product_count = len(equipment.product_ids)

    @api.depends('product_ids')
    def _compute_invoice_count(self):
        """Count invoices containing linked products"""
        for equipment in self:
            product_variant_ids = equipment.product_ids.mapped('product_variant_ids').ids
            invoice_lines = self.env['account.move.line'].search([
                ('product_id', 'in', product_variant_ids),
                ('move_id.move_type', 'in', ['out_invoice', 'in_invoice']),
                ('move_id.state', 'in', ['posted', 'in_payment'])
            ])
            invoices = invoice_lines.mapped('move_id')
            equipment.invoice_count = len(invoices)

    def action_view_products(self):
        """Open related products view"""
        self.ensure_one()
        return {
            'name': 'Linked Products',
            'type': 'ir.actions.act_window',
            'res_model': 'product.template',
            'view_mode': 'tree,form',
            'domain': [('equipment_id', '=', self.id)],
            'context': {
                'default_equipment_id': self.id,
                'default_is_equipment': True,
            },
        }

    def action_view_invoices(self):
        """Open related invoices view"""
        self.ensure_one()
        product_variant_ids = self.product_ids.mapped('product_variant_ids').ids
        invoice_lines = self.env['account.move.line'].search([
            ('product_id', 'in', product_variant_ids),
            ('move_id.move_type', 'in', ['out_invoice', 'in_invoice']),
            ('move_id.state', 'in', ['posted', 'in_payment'])
        ])
        invoices = invoice_lines.mapped('move_id')
        
        return {
            'name': 'Related Invoices',
            'type': 'ir.actions.act_window',
            'res_model': 'account.move',
            'view_mode': 'tree,form',
            'domain': [('id', 'in', invoices.ids)],
            'context': {},
        }
