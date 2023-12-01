# -*- coding: utf-8 -*-
# from odoo import http


# class CustomProductPlaceholder(http.Controller):
#     @http.route('/custom_product_placeholder/custom_product_placeholder', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/custom_product_placeholder/custom_product_placeholder/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('custom_product_placeholder.listing', {
#             'root': '/custom_product_placeholder/custom_product_placeholder',
#             'objects': http.request.env['custom_product_placeholder.custom_product_placeholder'].search([]),
#         })

#     @http.route('/custom_product_placeholder/custom_product_placeholder/objects/<model("custom_product_placeholder.custom_product_placeholder"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('custom_product_placeholder.object', {
#             'object': obj
#         })
