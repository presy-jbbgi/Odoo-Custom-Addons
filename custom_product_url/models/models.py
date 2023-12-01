# -*- coding: utf-8 -*-

# from odoo import models, fields, api


# class custom_product_url(models.Model):
#     _name = 'custom_product_url.custom_product_url'
#     _description = 'custom_product_url.custom_product_url'

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100

from odoo import api, fields, models
from odoo.addons.http_routing.models.ir_http import slug

class CustomProductTemplate(models.Model):
    _inherit = 'product.template'

    website_url = fields.Char(string='Website URL', compute='_compute_website_url', store=True)

    @api.depends('name')
    def _compute_website_url(self):
        super(CustomProductTemplate, self)._compute_website_url()
        for product in self:
            if product.id:
                new_slug = slug(product)
                product.website_url = f"/{new_slug}"
                # print("Computed website URL for product: ", product.name, new_slug)
                # return product.website_url

