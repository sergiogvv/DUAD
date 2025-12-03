SET search_path TO 'e-commerce_av3';

CREATE TABLE users
(
    "id" integer NOT NULL GENERATED ALWAYS AS IDENTITY ( INCREMENT 1 START 1 ),
    "full_name" character varying(50) NOT NULL,
    "email" character varying(50) UNIQUE NOT NULL,
	"password" character varying(12) NOT NULL,
    PRIMARY KEY (id)
);
ALTER TABLE IF EXISTS users
    OWNER to postgres;

CREATE TABLE roles
(
    "id" integer NOT NULL GENERATED ALWAYS AS IDENTITY ( INCREMENT 1 START 1 ),
    "user_id" integer NOT NULL,
    "role" VARCHAR(6) NOT NULL,
	PRIMARY KEY (id)
);
ALTER TABLE IF EXISTS roles
    OWNER to postgres;

CREATE TABLE carts(
    "id" integer NOT NULL GENERATED ALWAYS AS IDENTITY ( INCREMENT 1 START 1 ),
    "user_id" integer NOT NULL,
    "status" VARCHAR(10) NOT NULL,
	PRIMARY KEY (id)
);
ALTER TABLE IF EXISTS carts
    OWNER to postgres;

CREATE TABLE addresses(
    "id" integer NOT NULL GENERATED ALWAYS AS IDENTITY ( INCREMENT 1 START 1 ),
    "user_id" integer NOT NULL,
    "1st_line" VARCHAR(50) NOT NULL,
    "city" VARCHAR(50) NOT NULL,
    "state_or_prov" VARCHAR(50) NOT NULL,
    "postal_code" VARCHAR(10) NOT NULL,
    "billing_address" BOOLEAN NOT NULL,
	PRIMARY KEY (id)
);
ALTER TABLE IF EXISTS addresses
    OWNER to postgres;

CREATE TABLE payment_methods(
    "id" integer NOT NULL GENERATED ALWAYS AS IDENTITY ( INCREMENT 1 START 1 ),
    "user_id" integer NOT NULL,
    "type" VARCHAR(50) NOT NULL,
    "number" VARCHAR(50) NOT NULL,
	PRIMARY KEY (id)
);
ALTER TABLE IF EXISTS payment_methods
    OWNER to postgres;

CREATE TABLE sales(
    "id" integer NOT NULL GENERATED ALWAYS AS IDENTITY ( INCREMENT 1 START 1 ),
    "invoice_number" varchar(15) UNIQUE NOT NULL,
    "user_id" integer NOT NULL,
    "total_amount" DECIMAL(8, 2) NOT NULL,
    "order_date" date DEFAULT CURRENT_DATE,
    "status" varchar(15) NOT NULL,
    "address_id" integer NOT NULL,
    "payment_method_id" integer NOT NULL,
	PRIMARY KEY (id)
);
ALTER TABLE IF EXISTS sales
    OWNER to postgres;

CREATE TABLE cartsXproducts(
    "id" INTEGER NOT NULL GENERATED ALWAYS AS IDENTITY ( INCREMENT 1 START 1 ),
    "cart_id" INTEGER NOT NULL,
    "product_id" INTEGER NOT NULL,
    "quantity" INTEGER NOT NULL,
    "sale_id" INTEGER,
	PRIMARY KEY (id)
);
ALTER TABLE IF EXISTS cartsXproducts
    OWNER to postgres;

CREATE TABLE products(
    "id" integer NOT NULL GENERATED ALWAYS AS IDENTITY ( INCREMENT 1 START 1 ),
    "SKU" VARCHAR(50) UNIQUE NOT NULL,
    "name" VARCHAR(50) NOT NULL,
    "price" DECIMAL(8, 2) NOT NULL,
    "stock_quantity" INTEGER NOT NULL,
	PRIMARY KEY (id)
);
ALTER TABLE IF EXISTS cartsXproducts
    OWNER to postgres;




