--2. Construya una transacción para realizar el retorno de un producto, que funcione de la siguiente manera:

--    1. Validar que la factura existe en la DB (por ejemplo la factura 5)

IF EXISTS (
  SELECT *
  FROM transacciones.invoices
  WHERE 5 NOT IN (SELECT id FROM transacciones.invoices)
) THEN
  RETURN;  -- Salir de la transacción si no existe la factura 5
END IF;

--    2. Aumentar el stock del producto en la cantidad que se compró

UPDATE transacciones.products
SET quantity = quantity + (SELECT quantity FROM transacciones.invoices WHERE id = 5)
WHERE id = (SELECT product_id FROM transacciones.invoices WHERE id = 5);

SAVEPOINT stock_replenished;

--    3. Actualizar la factura y marcarla como retornada.

UPDATE transacciones.invoices
SET status = 'returned'
WHERE id = 5

COMMIT;