/* borrar la fact 2-1733 y la nc 2-2 */


/* Factura */
SELECT *
FROM account_invoice
WHERE afip_document_number = '0002-00001733';

/* linea de Factura */
SELECT *
FROM account_invoice_line
WHERE invoice_id = 3338;


/* Nota de credito */
SELECT *
FROM account_invoice
WHERE afip_document_number = '0002-00000002';

/* linea de nota de credito */
SELECT *
FROM account_invoice_line
WHERE invoice_id = 3341;


/* account move */
SELECT *
FROM account_move
WHERE afip_document_number = '0002-00001733';

/* account move line*/
SELECT *
FROM account_move_line
WHERE move_id = 5767;


/*-------------------------*/

/* Factura */
DELETE
FROM account_invoice
WHERE afip_document_number = '0002-00001733';

/* linea de Factura */
DELETE
FROM account_invoice_line
WHERE invoice_id = 3338;


/* Nota de credito */
DELETE
FROM account_invoice
WHERE afip_document_number = '0002-00000002';

/* linea de nota de credito */
DELETE
FROM account_invoice_line
WHERE invoice_id = 3341;


/* account move */
DELETE
FROM account_move
WHERE afip_document_number = '0002-00001733';

/* account move line*/
DELETE
FROM account_move_line
WHERE move_id = 5767;
