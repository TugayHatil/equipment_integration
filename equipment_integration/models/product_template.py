# -*- coding: utf-8 -*-
from odoo import models, fields, api


class ProductTemplate(models.Model):
    _inherit = 'product.template'

    is_equipment = fields.Boolean(
        string='Is Equipment',
        default=False,
        help='Mark this product as equipment for maintenance tracking'
    )
    equipment_id = fields.Many2one(
        'maintenance.equipment',
        string='Related Equipment',
        help='Equipment linked to this product'
    )
    show_create_equipment_btn = fields.Boolean(
        string='Show Create Equipment Button',
        compute='_compute_show_create_equipment_btn',
        store=False
    )

    @api.depends('is_equipment', 'equipment_id')
    def _compute_show_create_equipment_btn(self):
        """Show create button only when product is marked as equipment but not yet linked"""
        for record in self:
            record.show_create_equipment_btn = record.is_equipment and not record.equipment_id

    def action_create_equipment(self):
        """Open equipment creation wizard"""
        self.ensure_one()
        return {
            'name': 'Create Equipment',
            'type': 'ir.actions.act_window',
            'res_model': 'equipment.creation.wizard',
            'view_mode': 'form',
            'target': 'new',
            'context': {
                'default_product_id': self.id,
                'default_product_name': self.name,
            }
        }
