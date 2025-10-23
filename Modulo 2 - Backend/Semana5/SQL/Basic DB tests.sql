-- 1. Un script que agregue un usuario nuevo

INSERT INTO lyfter_car_rental.users (full_name, email, username, password, DOB, account_status) VALUES ('Sergio Velasqez', 'sergiogvv@gmail.com', 'sergiogvv666', 'wO3~xWNB40x=(7UnLx', '1985-03-20', 'active');

-- 2. Un script que agregue un automovil nuevo

INSERT INTO lyfter_car_rental.cars (car_make, model, year) VALUES ('Toyota', 'Rav4', 2020);

-- 3. Un script que cambie el estado de un usuario

UPDATE lyfter_car_rental.users SET account_status = 'defaulted' WHERE id = 123;

-- 4. Un script que cambie el estado de un automovil

UPDATE lyfter_car_rental.cars SET status = 'unavailable' WHERE id = 19;

-- 5. Un script que genere un alquiler nuevo con los datos de un usuario y un automovil

INSERT INTO lyfter_car_rental.rentals (rental_status,car_id,user_id) VALUES ('in use',6,144);
UPDATE lyfter_car_rental.cars SET status = 'unavailable' WHERE id = 6;

-- 6. Un script que confirme la devolución del auto al completar el alquiler, colocando el auto como disponible y completando el estado del alquiler

UPDATE lyfter_car_rental.rentals SET rental_status = 'returned' WHERE id = 5;
UPDATE lyfter_car_rental.cars SET status = 'available' WHERE id = (SELECT car_id FROM lyfter_car_rental.rentals WHERE id = 5);

-- 7. Un script que deshabilite un automovil del alquiler

DELETE FROM lyfter_car_rental.cars WHERE id = 10;

-- 8. Un script que obtenga todos los automoviles alquilados, y otro que obtenga todos los disponibles.
/* automoviles alquilados */
SELECT * FROM lyfter_car_rental.cars WHERE id IN 
(SELECT car_id FROM lyfter_car_rental.rentals
WHERE rental_status = 'in use');

/* automoviles disponibles para alquilar */
SELECT * FROM lyfter_car_rental.cars WHERE id NOT IN  
(SELECT car_id FROM lyfter_car_rental.rentals
WHERE rental_status IN ('in use','reserved'))
AND status != 'unavailable'




