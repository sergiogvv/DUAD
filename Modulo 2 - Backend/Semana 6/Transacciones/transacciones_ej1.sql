CREATE TABLE transacciones.products
(
    id integer NOT NULL GENERATED ALWAYS AS IDENTITY ( INCREMENT 1 START 1 ),
    name character varying(50) NOT NULL,
    price money NOT NULL,
    quantity  integer NOT NULL,
    PRIMARY KEY (id)
);

ALTER TABLE IF EXISTS transacciones.products
    OWNER to postgres;

CREATE TABLE transacciones.users
(
    id integer NOT NULL GENERATED ALWAYS AS IDENTITY ( INCREMENT 1 START 1 ),
    user_name character varying(50) NOT NULL,
    email character varying(50) NOT NULL,
    full_name character varying(50) NOT NULL,
    PRIMARY KEY (id)
);

ALTER TABLE IF EXISTS transacciones.users
    OWNER to postgres;

CREATE TABLE transacciones.invoices
(
    id integer NOT NULL GENERATED ALWAYS AS IDENTITY ( INCREMENT 1 START 1 ),
    product_id integer NOT NULL,
    user_id integer NOT NULL,
    status character varying(10) NOT NULL,
	quantity integer NOT NULL,
	total money NOT NULL,
    PRIMARY KEY (id)
);

ALTER TABLE IF EXISTS transacciones.invoices
    OWNER to postgres;

insert into transacciones.invoices (product_id, user_id, status, quantity, total) values (14, 1, 'fulfilled', 10, 149.90);
insert into transacciones.invoices (product_id, user_id, status, quantity, total) values (9, 4, 'fulfilled', 5, 32.45);
insert into transacciones.invoices (product_id, user_id, status, quantity, total) values (4, 2, 'fulfilled', 1, 29.99);
insert into transacciones.invoices (product_id, user_id, status, quantity, total) values (17, 2, 'fulfilled', 5, 22.45);


insert into transacciones.products (name, price, quantity) values ('Maple Chipotle Glaze', 3.49, 76);
insert into transacciones.products (name, price, quantity) values ('Garlic & Herb Goat Cheese', 5.49, 35);
insert into transacciones.products (name, price, quantity) values ('Chia Seeds', 6.99, 45);
insert into transacciones.products (name, price, quantity) values ('Portable Water Filter', 29.99, 93);
insert into transacciones.products (name, price, quantity) values ('Rice Noodles', 3.49, 29);
insert into transacciones.products (name, price, quantity) values ('Red Lentils', 1.99, 23);
insert into transacciones.products (name, price, quantity) values ('Fishing Rod', 49.99, 63);
insert into transacciones.products (name, price, quantity) values ('Folding Backpack Chair', 49.99, 33);
insert into transacciones.products (name, price, quantity) values ('Pecan Nuts', 6.49, 9);
insert into transacciones.products (name, price, quantity) values ('Electric Heat Pad', 24.99, 94);
insert into transacciones.products (name, price, quantity) values ('Pest Control Traps', 22.99, 43);
insert into transacciones.products (name, price, quantity) values ('Organic Granola', 5.49, 64);
insert into transacciones.products (name, price, quantity) values ('Mayonnaise', 3.29, 10);
insert into transacciones.products (name, price, quantity) values ('Eco-Friendly Beeswax Wraps', 14.99, 59);
insert into transacciones.products (name, price, quantity) values ('Classic Pumps', 64.99, 96);
insert into transacciones.products (name, price, quantity) values ('Savory Oatmeal', 2.49, 19);
insert into transacciones.products (name, price, quantity) values ('Organic Fruit Salad', 4.49, 19);
insert into transacciones.products (name, price, quantity) values ('Pet Hair Vacuum Cleaner Attachment', 14.99, 52);
insert into transacciones.products (name, price, quantity) values ('Whole Wheat Bread', 2.49, 55);
insert into transacciones.products (name, price, quantity) values ('Pet Travel Bowl', 10.99, 100);

insert into transacciones.users (user_name, email, full_name) values ('kdrache0', 'kdrache0@bloomberg.com', 'Kacy Drache');
insert into transacciones.users (user_name, email, full_name) values ('mstenbridge1', 'mstenbridge1@bloglines.com', 'Matilde Stenbridge');
insert into transacciones.users (user_name, email, full_name) values ('gboughey2', 'gboughey2@amazon.co.uk', 'Gisele Boughey');
insert into transacciones.users (user_name, email, full_name) values ('cjosefer3', 'cjosefer3@feedburner.com', 'Cayla Josefer');
insert into transacciones.users (user_name, email, full_name) values ('lmellody4', 'lmellody4@google.pl', 'Lula Mellody');



