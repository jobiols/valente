/*  creó una nota de crédito y no le forzó el periodo con lo que quedó con la fecha de
    hoy pero con el periodo pasado.
*/


/* nota de credito */
SELECT date_due
  ,afip_document_number,ap.name
  ,amount_total
FROM account_invoice ai
join account_period ap
on ap.id = ai.period_id
WHERE afip_document_number = '0004-00000007'
AND type = 'out_refund';

SELECT *
FROM account_invoice_line

SELECT * FROM account_period

/* contabilidad no se toca */

select aml.period_id from account_move am
  JOIN account_move_line aml
  ON am.id = aml.move_id
where am.afip_document_number = '0004-00000007'
AND am.name LIKE 'RVE%';


/* corregir periodo */
update account_invoice
set period_id = 8
WHERE afip_document_number = '0004-00000007'
AND type = 'out_refund';
