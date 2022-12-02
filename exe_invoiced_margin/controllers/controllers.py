# -*- coding: utf-8 -*-
# from odoo import http


# class ExeAgroconsultasInvoicedMargin(http.Controller):
#     @http.route('/exe_agroconsultas_invoiced_margin/exe_agroconsultas_invoiced_margin/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/exe_agroconsultas_invoiced_margin/exe_agroconsultas_invoiced_margin/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('exe_agroconsultas_invoiced_margin.listing', {
#             'root': '/exe_agroconsultas_invoiced_margin/exe_agroconsultas_invoiced_margin',
#             'objects': http.request.env['exe_agroconsultas_invoiced_margin.exe_agroconsultas_invoiced_margin'].search([]),
#         })

#     @http.route('/exe_agroconsultas_invoiced_margin/exe_agroconsultas_invoiced_margin/objects/<model("exe_agroconsultas_invoiced_margin.exe_agroconsultas_invoiced_margin"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('exe_agroconsultas_invoiced_margin.object', {
#             'object': obj
#         })
