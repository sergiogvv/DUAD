CREATE TABLE lyfter_car_rental.cars
(
    id integer NOT NULL GENERATED ALWAYS AS IDENTITY,
    car_make character varying(30) NOT NULL,
    model character varying(30) NOT NULL,
    year integer NOT NULL,
    status character varying(30) NOT NULL DEFAULT 'available',
    PRIMARY KEY (id)
);

ALTER TABLE IF EXISTS lyfter_car_rental.cars
    OWNER to postgres;

SET search_path TO lyfter_car_rental;

insert into cars (car_make, model, year, status) values ('Ford', 'Mustang', 1974, 'unavailable');
insert into cars (car_make, model, year, status) values ('Lexus', 'RX', 1999, 'unavailable');
insert into cars (car_make, model, year, status) values ('Mitsubishi', 'Galant', 1986, 'unavailable');
insert into cars (car_make, model, year, status) values ('Ford', 'E-Series', 1991, 'unavailable');
insert into cars (car_make, model, year, status) values ('Chevrolet', 'Suburban 2500', 1993, 'unavailable');
insert into cars (car_make, model, year) values ('Scion', 'tC', 2012);
insert into cars (car_make, model, year) values ('Chrysler', 'LHS', 2000);
insert into cars (car_make, model, year) values ('Plymouth', 'Grand Voyager', 1992);
insert into cars (car_make, model, year) values ('Ford', 'E-Series', 1985);
insert into cars (car_make, model, year) values ('Chevrolet', 'Astro', 1996);
insert into cars (car_make, model, year) values ('Lexus', 'HS', 2010);
insert into cars (car_make, model, year) values ('Ford', 'Expedition', 2004);
insert into cars (car_make, model, year) values ('Buick', 'Riviera', 1979);
insert into cars (car_make, model, year) values ('Acura', 'CL', 2001);
insert into cars (car_make, model, year) values ('Mitsubishi', 'Eclipse', 2012);
insert into cars (car_make, model, year) values ('Toyota', 'RAV4', 2000);
insert into cars (car_make, model, year) values ('Nissan', 'Altima', 1999);
insert into cars (car_make, model, year) values ('Ford', 'EXP', 1986);
insert into cars (car_make, model, year) values ('Ford', 'E-Series', 2001);
insert into cars (car_make, model, year) values ('Nissan', 'Cube', 2010);
insert into cars (car_make, model, year) values ('Chevrolet', 'Suburban', 2007);
insert into cars (car_make, model, year) values ('Jeep', 'Wrangler', 2008);
insert into cars (car_make, model, year) values ('Hyundai', 'Santa Fe', 2003);
insert into cars (car_make, model, year) values ('Volkswagen', 'Tiguan', 2010);
insert into cars (car_make, model, year) values ('GMC', 'Vandura 2500', 1993);
insert into cars (car_make, model, year) values ('Mitsubishi', 'Montero', 2005);
insert into cars (car_make, model, year) values ('Volkswagen', 'CC', 2011);
insert into cars (car_make, model, year) values ('BMW', 'X5 M', 2013);
insert into cars (car_make, model, year) values ('Cadillac', 'Seville', 2001);
insert into cars (car_make, model, year) values ('Toyota', '4Runner', 1997);

