-- SQLite
/* 1. Cree una nueva base de datos en SQLite.
2. Replique las tablas creadas anteriormente en [Ejercicios de Bases de Datos], 
con sus respectivos PKs, FKs, constraints, y demás requerimientos.
    1. Investigue cómo hacer que los `PKs` se generen **automáticamente**.
    2. Utilice los tipos de datos adecuados. 
    3. Si existe alguna limitante por SQLite, documéntela y 
    resuelva la limitante como considere adecuado.*/

CREATE TABLE products (
    id INTEGER PRIMARY KEY AUTOINCREMENT, 
    SKU VARCHAR(15) UNIQUE NOT NULL,
    name VARCHAR(25) NOT NULL,
    price INT DEFAULT 0,
    entry_date VARCHAR (9) NOT NULL,
    brand VARCHAR (25)
);

CREATE TABLE invoices (
    id INTEGER PRIMARY KEY AUTOINCREMENT, 
    user_id INT REFERENCES Products(id),
    invoice_no INT UNIQUE NOT NULL,
    order_date VARCHAR (9) NOT NULL,
    buyer_email VARCHAR (25),
    invoice_amount INT NOT NULL
);

CREATE TABLE invoiced_products (
    id INTEGER PRIMARY KEY AUTOINCREMENT, 
    product_id INT REFERENCES Products(id),
    invoice_id INT REFERENCES Invoices(id),
    quantity INT NOT NULL
);

CREATE TABLE cart (
    id INTEGER PRIMARY KEY AUTOINCREMENT, 
    buyer_email VARCHAR (25),
    product_id INT REFERENCES Products(id)
);

CREATE TABLE users (
    id INTEGER PRIMARY KEY AUTOINCREMENT, 
    full_name VARCHAR (50) NOT NULL,
    buyer_email VARCHAR (25) UNIQUE NOT NULL,
    register_date VARCHAR (9) NOT NULL
);

CREATE TABLE reviews (
    id INTEGER PRIMARY KEY AUTOINCREMENT, 
    product_id INT REFERENCES Products(id),
    user_id INT REFERENCES Products(id),
    comment TEXT NOT NULL,
    rating SMALLINT DEFAULT 5,
    DATE CURRENT_TIMESTAMP
);

CREATE TABLE payment_methods (
    id INTEGER PRIMARY KEY AUTOINCREMENT, 
    invoice_id INT REFERENCES Invoices(id),
    type VARCHAR(25) NOT NULL,
    bank_name VARCHAR(50)
);

CREATE TABLE categories (
    id INTEGER PRIMARY KEY AUTOINCREMENT, 
    name UNIQUE NOT NULL,
    description TEXT
);

ALTER TABLE products
    ADD category_id INTEGER REFERENCES categories(id);
    
/* 3. Modifique la tabla de Facturas creada en el ejercicio anterior y 
agregue una columna para almacenar también el número de teléfono del comprador, 
y otra para el código de empleado del cajero que realizó la venta. */

ALTER TABLE invoices
    ADD buyer_phone_no BIGINT;

ALTER TABLE invoices
    ADD cashier_no INT;

/* 4. Realice los siguientes `SELECT`:
    a. Obtenga todos los productos almacenados */
    SELECT * 
        FROM products;

    /* b. Obtenga todos los productos que tengan un precio mayor a 50000 */
    SELECT * 
        FROM products 
        WHERE price > 50000;

    /* c. Obtenga todas las compras de un mismo producto por id. */
    SELECT *
        FROM invoiced_products
        WHERE product_id = 1;

    /*d. Obtenga todas las compras agrupadas por producto, 
    donde se muestre el total comprado entre todas las compras. */
    SELECT product_id, sum(quantity)
        FROM invoiced_products
        GROUP BY product_id;

    /* e. Obtenga todas las facturas realizadas por el mismo comprador */
    SELECT *
        FROM invoices
        WHERE user_id = 1

    /* f. Obtenga todas las facturas ordenadas por monto total de forma descendente */
    SELECT *
        FROM invoices
        ORDER BY invoice_amount DESC;

    /* g. Obtenga una sola factura por número de factura. */
    SELECT *
        FROM invoices
        WHERE invoice_no = 1


