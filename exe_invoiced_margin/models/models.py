# -*- coding: utf-8 -*-

from odoo import models, fields, api,_
from odoo.exceptions import UserError
import logging

_logger = logging.getLogger(__name__)

class SaleOrderCustomization(models.Model):
    _inherit = 'sale.order'

    @api.depends('invoice_margin','invoice_ids.amount_total')
    def get_invoice_margin(self):
        for rec in self:
            total_margin=0.0
            for invoice in rec.invoice_ids:
                if(invoice.type=='out_invoice'):
                    total_margin=total_margin+invoice.amount_total
                    _logger.info(str(total_margin))
            rec.invoice_margin=rec.amount_total-total_margin


    invoice_margin = fields.Float(string="Saldo a Facturar", compute="get_invoice_margin", store=True)

