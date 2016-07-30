/* parche para eliminar la percepcion rio negro de la factura 196 */

delete from account_invoice_tax
where id = 1106;