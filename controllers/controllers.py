# -*- coding: utf-8 -*-
from odoo import http

# class RealEstateTraining(http.Controller):
#     @http.route('/real_estate_training/real_estate_training/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/real_estate_training/real_estate_training/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('real_estate_training.listing', {
#             'root': '/real_estate_training/real_estate_training',
#             'objects': http.request.env['real_estate_training.real_estate_training'].search([]),
#         })

#     @http.route('/real_estate_training/real_estate_training/objects/<model("real_estate_training.real_estate_training"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('real_estate_training.object', {
#             'object': obj
#         })