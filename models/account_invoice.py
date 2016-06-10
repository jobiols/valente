# -*- coding: utf-8 -*-
# -----------------------------------------------------------------------------------
#
#    Copyright (C) 2016  jeo Software  (http://www.jeo-soft.com.ar)
#    All Rights Reserved.
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
# -----------------------------------------------------------------------------------
import logging

from openerp import models, fields, api
import openerp.addons.decimal_precision as dp

_logger = logging.getLogger(__name__)


class account_invoice(models.Model):
    _inherit = "account.invoice"

    cc_tax_10 = fields.Float(
        compute="_get_values",
        digits=dp.get_precision('Account'),
        string='IVA 10.5%',
    )

    cc_tax_21 = fields.Float(
        compute="_get_values",
        digits=dp.get_precision('Account'),
        string='IVA 21%',
    )

    cc_tax_27 = fields.Float(
        compute="_get_values",
        digits=dp.get_precision('Account'),
        string='IVA 27%',
    )

    cc_tax_exempt = fields.Float(
        compute="_get_values",
        digits=dp.get_precision('Account'),
        string='No Gravado',
    )

    cc_perc_IIBB = fields.Float(
        compute="_get_values",
        digits=dp.get_precision('Account'),
        string=u'Percepción IIBB',
    )

    cc_perc_iva = fields.Float(
        compute="_get_values",
        digits=dp.get_precision('Account'),
        string=u'Percepción IVA',
    )

    cc_base = fields.Float(
        compute="_get_values",
        digits=dp.get_precision('Account'),
        string=u'Base imponible',
    )

    @api.one
    def _get_values(self):

        if False:
            print '------------------------------------------------------ ', doc_code
            print 'printed_amount_untaxed={} ' \
                  'printed_amount_tax={} ' \
                  'vat_amount={} ' \
                  'other_taxes_amount={} ' \
                  'vat_exempt_amount={} ' \
                  'vat_untaxed={} ' \
                  'vat_base_amount={}'.format(
                self.printed_amount_untaxed,
                self.printed_amount_tax,
                self.vat_amount,
                self.other_taxes_amount,
                self.vat_exempt_amount,
                self.vat_untaxed,
                self.vat_base_amount)
            print 'printed_tax_ids --'
            for tax in self.printed_tax_ids:
                print tax.base, tax.amount, tax.name

            print 'vat_tax_ids --'
            for tax in self.vat_tax_ids:
                print tax.base, tax.amount, tax.name

            print 'not_vat_tax_ids --'
            for tax in self.not_vat_tax_ids:
                print tax.base, tax.amount, tax.name

        # calcular el iva para las tres columnas 10.5 21 y 27
        # y la base imponible gravada
        for tax in self.vat_tax_ids:
            if ('IVA Compras 10.5%' in tax.name or 'IVA Ventas 10.5%' in tax.name):
                self.cc_tax_10 += tax.amount

            if ('IVA Compras 21%' in tax.name or 'IVA Ventas 21%' in tax.name):
                self.cc_tax_21 += tax.amount

            if ('IVA Compras 27%' in tax.name or 'IVA Compras 27%' in tax.name):
                self.cc_tax_27 += tax.amount

            # Calcular la base imponible sumanto las bases de todos los iva gravados
            if 'IVA' in tax.name:
                if tax.amount != 0:
                    self.cc_base += tax.base

        # calcular percepciones IIBB e Iva
        for tax in self.not_vat_tax_ids:
            if 'Perc IIBB' in tax.name:
                self.cc_perc_IIBB += tax.amount

            if 'Perc IVA' in tax.name:
                self.cc_perc_iva += tax.amount

        # calcular exento por diferencia
        tax_exempt = self.cc_amount_total - \
                     self.cc_base - \
                     self.cc_perc_iva - \
                     self.cc_perc_IIBB - \
                     self.cc_tax_27 - \
                     self.cc_tax_21 - \
                     self.cc_tax_10

        # filtrar el error de redondeo
        if (abs(tax_exempt) > 0.05):
            self.cc_tax_exempt = tax_exempt

# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
