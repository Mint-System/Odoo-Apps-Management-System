# from odoo import http


# class Mgmt(http.Controller):
#     @http.route('/mgmt/mgmt', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/mgmt/mgmt/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('mgmt.listing', {
#             'root': '/mgmt/mgmt',
#             'objects': http.request.env['mgmt.mgmt'].search([]),
#         })

#     @http.route('/mgmt/mgmt/objects/<model("mgmt.mgmt"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('mgmt.object', {
#             'object': obj
#         })
