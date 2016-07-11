esto se pone en el archivo:
l10n_ar_invoice/models/invoice.py 351

        """
        print '------------------------------------------------------------------'
        print 'printed_tax_ids  ', self.printed_tax_ids
        for ids in self.printed_tax_ids:
            print '-->', ids.name
        print 'vat_tax_ids      ', self.vat_tax_ids
        for ids in self.vat_tax_ids:
            print '-->', ids.name
        print 'not_vat_tax_ids  ', self.not_vat_tax_ids
        for ids in self.not_vat_tax_ids:
            print '-->', ids.name

        print 'printed_amount_untaxed   ', self.printed_amount_untaxed
        print 'printed_amount_tax       ', self.printed_amount_tax
        print 'vat_amount               ', self.vat_amount
        print 'other_taxes_amount       ', self.other_taxes_amount
        print 'vat_exempt_amount        ', self.vat_exempt_amount
        print 'vat_untaxed              ', self.vat_untaxed
        print 'vat_base_amount          ', self.vat_base_amount
        print '------------------------------------------------------------------'
        """


#Factura A

printed_tax_ids   account.invoice.tax(888, 887)
--> IVA Ventas 21%
--> Perc IIBB Rio Negro - Percepción IIBB Rio Negro
vat_tax_ids       account.invoice.tax(888,)
--> IVA Ventas 21%
not_vat_tax_ids   account.invoice.tax(887,)
--> Perc IIBB Rio Negro - Percepción IIBB Rio Negro
printed_amount_untaxed    100.0
printed_amount_tax        31.0
vat_amount                21.0
other_taxes_amount        10.0
vat_exempt_amount         0.0
vat_untaxed               0.0
vat_base_amount           100.0


#Factura B

printed_tax_ids   account.invoice.tax()
vat_tax_ids       account.invoice.tax(891,)
--> IVA Ventas 21%
not_vat_tax_ids   account.invoice.tax(889,)
--> Perc IIBB Rio Negro - Percepción IIBB Rio Negro
printed_amount_untaxed    131.0
printed_amount_tax        0.0
vat_amount                21.0
other_taxes_amount        10.0
vat_exempt_amount         0.0
vat_untaxed               0.0
vat_base_amount           100.0
