# -*- coding: utf-8 -*-
# from odoo import http


# class CustomProductUrl(http.Controller):
#     @http.route('/custom_product_url/custom_product_url', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/custom_product_url/custom_product_url/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('custom_product_url.listing', {
#             'root': '/custom_product_url/custom_product_url',
#             'objects': http.request.env['custom_product_url.custom_product_url'].search([]),
#         })

#     @http.route('/custom_product_url/custom_product_url/objects/<model("custom_product_url.custom_product_url"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('custom_product_url.object', {
#             'object': obj
#         })

from odoo import http
from odoo.http import request
from odoo.addons.website_sale.controllers.main import WebsiteSale

class redirect_product_url(WebsiteSale):

    @http.route(['/<model("product.template"):product>'], type='http', website=True, sitemap=False)
    def product(self, product, category='', search='', **kwargs):
        return super(redirect_product_url, self).product(product, category=category, search=search, **kwargs)

    @http.route(['/shop/<model("product.template"):product>'], type='http', website=True, sitemap=False)
    def redirect_product_url(self,product):
        return request.redirect(f'{product.website_url.replace("/shop/","/")}', code=301)
