# -*- coding: utf-8 -*-
from odoo import http
from odoo.http import request
from odoo.addons.sale.controllers.variant import VariantController


class CustomShowDefaultCode(VariantController):
    @http.route(['/sale/get_combination_info_website'], type='json', auth="public", methods=['POST'], website=True)
    def get_combination_info_website(self, product_template_id, product_id, combination, add_qty, **kw):
        """Special route to use website logic in get_combination_info override.
        This route is called in JS by appending _website to the base route.
        """
        kw.pop('pricelist_id')
        combination = self.get_combination_info(product_template_id, product_id, combination, add_qty,
                                                request.website.get_current_pricelist(), **kw)

        if request.website.google_analytics_key:
            combination['product_tracking_info'] = request.env['product.template'].get_google_analytics_data(
                combination)

        if request.website.product_page_image_width != 'none' and not request.env.context.get('website_sale_no_images', False):
            carousel_view = request.env['ir.ui.view']._render_template('website_sale.shop_product_images', values={
                'product': request.env['product.template'].browse(combination['product_template_id']),
                'product_variant': request.env['product.product'].browse(combination['product_id']),
                'website': request.env['website'].get_current_website(),
            })
            combination['carousel'] = carousel_view

        default_code = request.env['product.product'].browse(combination['product_id']).default_code
        combination['default_code'] = default_code or False

        return combination



#     @http.route('/custom_show_default_code/custom_show_default_code', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/custom_show_default_code/custom_show_default_code/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('custom_show_default_code.listing', {
#             'root': '/custom_show_default_code/custom_show_default_code',
#             'objects': http.request.env['custom_show_default_code.custom_show_default_code'].search([]),
#         })

#     @http.route('/custom_show_default_code/custom_show_default_code/objects/<model("custom_show_default_code.custom_show_default_code"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('custom_show_default_code.object', {
#             'object': obj
#         })
