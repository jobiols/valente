/* parche para cambiar dos numeros de factura entre si
  en el pv 5 se cargan las facturas que se hicieron en linea (AFIP),
  habia 2 facturas para cargar, cargó primero la 449 y el sistema
  la validó como 448

  0005-00000448
  0005-00000449

  Borramos la 449 y cargamos a mano de nuevo
*/

/* borrar factura 448
select * from account_invoice
where id = 1160;
select * from account_invoice_line
WHERE invoice_id = 1160;

borrar asientos factura 448
select * from account_move
where afip_document_number = '0005-00000448';
select * from account_move_line
where move_id = 1900;
*/

/* borrar factura 448 */
delete from account_invoice
where id = 1160;
delete from account_invoice_line
WHERE invoice_id = 1160;

/* borrar asientos factura 448 */
delete from account_move
where afip_document_number = '0005-00000448';
delete from account_move_line
where move_id = 1900;
