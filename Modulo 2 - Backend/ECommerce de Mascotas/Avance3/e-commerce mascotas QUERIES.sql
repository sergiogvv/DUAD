SET search_path TO 'e-commerce_av3';

-- Busqueda de usuario por medio de un email

SELECT * FROM users
WHERE email = 'sabramof1@facebook.com' -- En este caso se obtiene id = 2


-- Si un usuario solamente puede tener un carrito, entonces se requiere un query que obtenga específicamente el carrito de un usuario.

SELECT * FROM carts
WHERE user_id = 2 AND status = 'active';

-- Si las facturas están relacionadas con un único usuario, se requiere un query que obtenga todas las facturas de ese usuario.

SELECT * FROM sales
WHERE user_id = 2


-- Si una factura tiene relación con los productos comprados, entonces se requiere un query que obtenga todos los productos comprados en una sola factura.

SELECT p."SKU", p.name, p.price, cp.quantity
FROM products AS p
JOIN cartsxproducts AS cp
ON p.id = cp.product_id
WHERE cp.sale_id = 5; -- obtener todos los productos de la factura correspondiente a sale_id = 5


SELECT * FROM
(SELECT p."SKU", p.name, p.price, cp.quantity
FROM products AS p
JOIN cartsxproducts AS cp
ON p.id = cp.product_id
WHERE cp.sale_id = 5) as prod_data
CROSS JOIN
(SELECT invoice_number, order_date FROM sales
WHERE id= 5) as sale_data; -- obtener todos los productos de la factura correspondiente a sale_id = 5, y agregar las columnas invoice_number y order_date correspondientes a dicha factura


-- Consulta de productos dentro del carrito activo de un usuario: Usamos el carrito activo del usuario 2 como ejemplo
SELECT p."SKU", p.name, p.price, cp.quantity
FROM products AS p
JOIN cartsxproducts AS cp
ON p.id = cp.product_id
WHERE cp.cart_id = (SELECT id FROM carts WHERE user_id = 2 AND status = 'active');

-- Consulta de metodos de pago para un usuario

SELECT * FROM payment_methods
WHERE user_id = 2
ORDER BY id ASC;

-- Consulta de direcciones para un usuario

SELECT * FROM addresses
WHERE user_id = 2
ORDER BY id ASC;

