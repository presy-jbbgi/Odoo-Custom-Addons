# -*- coding: utf-8 -*-

from odoo import models, fields, api


class custom_product_placeholder(models.Model):
    _inherit = 'product.product'

    @api.model
    def _get_placeholder_filename(self, field):
        image_fields = ['image_%s' % size for size in [1920, 1024, 512, 256, 128]]
        if field in image_fields:
            return 'custom_product_placeholder/static/img/placeholder.jpg'
        return super()._get_placeholder_filename(field)

#     _name = 'custom_product_placeholder.custom_product_placeholder'
#     _description = 'custom_product_placeholder.custom_product_placeholder'

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100

