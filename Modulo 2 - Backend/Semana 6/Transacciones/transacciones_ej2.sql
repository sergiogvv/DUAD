--1. Construya una transacción para realizar una compra, que debe funcionar de la siguiente manera:

BEGIN TRANSACTION;
-- 1. Validar que existe stock del producto (por ejemplo producto 3)
IF EXISTS (
  SELECT *
  FROM transacciones.products
  WHERE id = 3
  AND quantity  < 0
) THEN
  RETURN;  -- Salir de la transacción si no existe un producto en el resultado.
END IF;

-- 2. Validar que el usuario existe (por ejemplo el usuario id = 1)
IF EXISTS (
  SELECT *
  FROM transacciones.users
  WHERE 1 NOT IN (SELECT id FROM transacciones.users)
) THEN
  RETURN;  -- Salir de la transacción si no existe el usuario id = 1 
END IF;

-- 3. Crear la factura con el usuario relacionado

INSERT INTO transacciones.invoices (product_id, user_id, status, quantity, total)
VALUES (3, 1, 'Pending',6, 6 * (SELECT price FROM transacciones.products WHERE id =3)); -- compra de producto 3 por 6 unidades

SAVEPOINT invoice_created;

-- 4. Reducir el stock del producto

UPDATE transacciones.products
SET quantity = quantity - 6
WHERE id = 3;

COMMIT;





