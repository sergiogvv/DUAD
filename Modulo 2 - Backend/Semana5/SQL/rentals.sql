CREATE TABLE lyfter_car_rental.rentals
(
    id integer NOT NULL GENERATED ALWAYS AS IDENTITY ( INCREMENT 1 START 1 ),
    rental_date date NOT NULL DEFAULT CURRENT_DATE,
    rental_status character varying(30) NOT NULL,
    car_id integer NOT NULL,
    user_id integer NOT NULL,
    PRIMARY KEY (id)
);

ALTER TABLE IF EXISTS lyfter_car_rental.rentals
    OWNER to postgres;

SET search_path TO lyfter_car_rental;

insert into rentals (rental_status,car_id,user_id) values ('in use',1,149);
insert into rentals (rental_status,car_id,user_id) values ('in use',2,148);
insert into rentals (rental_status,car_id,user_id) values ('in use',3,147);
insert into rentals (rental_status,car_id,user_id) values ('in use',4,146);
insert into rentals (rental_status,car_id,user_id) values ('in use',5,145);
insert into rentals (rental_date, rental_status, car_id, user_id) values ('2022-03-12', 'returned', 30, 104);
insert into rentals (rental_date, rental_status, car_id, user_id) values ('2024-12-24', 'returned', 29, 131);
insert into rentals (rental_date, rental_status, car_id, user_id) values ('2025-02-14', 'returned', 1, 110);
insert into rentals (rental_date, rental_status, car_id, user_id) values ('2025-05-25', 'returned', 10, 141);
insert into rentals (rental_date, rental_status, car_id, user_id) values ('2018-01-03', 'returned', 9, 137);
insert into rentals (rental_date, rental_status, car_id, user_id) values ('2018-09-26', 'returned', 20, 109);
insert into rentals (rental_date, rental_status, car_id, user_id) values ('2025-10-16', 'returned', 18, 146);
insert into rentals (rental_date, rental_status, car_id, user_id) values ('2021-04-23', 'returned', 24, 113);
insert into rentals (rental_date, rental_status, car_id, user_id) values ('2018-05-18', 'returned', 4, 137);
insert into rentals (rental_date, rental_status, car_id, user_id) values ('2019-11-28', 'returned', 14, 132);
insert into rentals (rental_date, rental_status, car_id, user_id) values ('2025-11-10', 'reserved', 9, 111);
insert into rentals (rental_date, rental_status, car_id, user_id) values ('2025-11-13', 'reserved', 23, 142);
insert into rentals (rental_date, rental_status, car_id, user_id) values ('2025-12-29', 'reserved', 15, 129);
insert into rentals (rental_date, rental_status, car_id, user_id) values ('2025-11-01', 'reserved', 30, 124);
insert into rentals (rental_date, rental_status, car_id, user_id) values ('2025-12-17', 'reserved', 22, 144);
insert into rentals (rental_date, rental_status, car_id, user_id) values ('2025-11-06', 'reserved', 22, 115);
insert into rentals (rental_date, rental_status, car_id, user_id) values ('2025-12-26', 'reserved', 22, 113);
insert into rentals (rental_date, rental_status, car_id, user_id) values ('2025-12-03', 'reserved', 24, 128);
insert into rentals (rental_date, rental_status, car_id, user_id) values ('2025-11-25', 'reserved', 26, 123);
insert into rentals (rental_date, rental_status, car_id, user_id) values ('2025-12-12', 'reserved', 14, 111);


