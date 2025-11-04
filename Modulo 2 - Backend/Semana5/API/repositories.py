

class UserRepository:
    def __init__(self, db_manager):
        self.db_manager = db_manager

    def _format_record(self, record):
        return {
            "id": record[0],
            "full_name": record[1],
            "email": record[2],
            "username": record[3],
            "password": record[4],
            "DOB": record[5],
            "account_status": record[6]
        }

    def create(self, full_name, email, username, password, DOB, account_status): #Crear un usuario nuevo
        try:
            self.db_manager.execute_query(
                "INSERT INTO lyfter_car_rental.users (full_name, email, username, password, DOB, account_status) VALUES (%s, %s, %s, %s, %s, %s);",
                (full_name, email, username, password, DOB, account_status),
            )
            result = self.db_manager.execute_query("SELECT LASTVAL();")
            new_id = result[0][0] if result else None
            print('Record created successfully')
            return {"success": True, "message": "User created successfully", "id": new_id}
        except Exception as error:
            print("Error inserting record into the database: ", error)
            return {"success": False, "error": str(error)}

    def get_all(self): #Listar todos los usuarios
        try:
            results = self.db_manager.execute_query(
                "SELECT * FROM lyfter_car_rental.users;"
            )
            formatted_results = [self._format_record(result) for result in results]
            return formatted_results
        except Exception as error:
            print("Error getting all records from the database: ", error)
            return False
        
    def get_by_id(self, id):
        try:
            results = self.db_manager.execute_query(
                "SELECT * FROM lyfter_car_rental.users WHERE id = %s;",
                (id,)
            )
            formatted_result = [self._format_record(result) for result in results]
            return formatted_result
        except Exception as error:
            print("Error getting user from the database: ", error)
            return False
        
    def get_by_username(self, username): #El listado de usuarios debe ser capaz de filtrar por username
        try:
            results = self.db_manager.execute_query(
                "SELECT * FROM lyfter_car_rental.users WHERE username = %s;",
                (username,)
            )
            formatted_result = [self._format_record(result) for result in results]
            return formatted_result
        except Exception as error:
            print("Error getting user from the database: ", error)
            return False

    def get_by_email(self, email): 
        try:
            results = self.db_manager.execute_query(
                "SELECT * FROM lyfter_car_rental.users WHERE email = %s;",
                (email,)
            )
            formatted_result = [self._format_record(result) for result in results]
            print(formatted_result)
            return formatted_result
        except Exception as error:
            return False

    def change_account_status(self, id, account_status): #Cambiar el estado de un usuario
        try:
            self.db_manager.execute_query(
                "UPDATE lyfter_car_rental.users SET account_status = %s WHERE id = %s",
                (account_status, id)
            )
            if self.db_manager.cursor.rowcount == 0:
                return {"success": False, "error": "User not found"}
            print(f'Account status updated to {account_status} for user {id}')
            return {"success": True, "message": "Account status successfully updated", "id": id, "account_status": account_status}
        except Exception as error:
            print("Error updating user status: ", error)
            return {"success": False, "error": str(error)}
    
    def flag_as_defaulted(self, id, account_status='defaulted'): #Flagear un usuario como moroso
        try:
            self.db_manager.execute_query(
                "UPDATE lyfter_car_rental.users SET account_status = %s WHERE id = %s",
                (account_status, id)
            )
            print(f'User {id} flagged as {account_status}')
            return True
        except Exception as error:
            print("Error updating user status: ", error)
            return {"success": False, "error": str(error)}

class CarRepository:
    def __init__(self, db_manager):
        self.db_manager = db_manager

    def _format_record(self, record):
        return {
            "id": record[0],
            "car_make": record[1],
            "model": record[2],
            "year": record[3],
            "status": record[4]
        }

    def create(self, car_make, model, year): #Crear un automovil nuevo
        try:
            self.db_manager.execute_query(
                "INSERT INTO lyfter_car_rental.cars (car_make, model, year) VALUES (%s, %s, %s)",
                (car_make, model, year)
            )
            result = self.db_manager.execute_query("SELECT LASTVAL();")
            new_id = result[0][0] if result else None
            print(f'Record created successfully')
            return {"success": True, "message": "Car created successfully", "id": new_id}
        except Exception as error:
            print("Error inserting record into the database: ", error)
            return {"success": False, "error": str(error)}
        
    def get_all(self): #Listar todos los automoviles
        try:
            results = self.db_manager.execute_query(
                "SELECT * FROM lyfter_car_rental.cars;"
            )
            formatted_results = [self._format_record(result) for result in results]
            return formatted_results
        except Exception as error:
            print("Error getting all records from the database: ", error)
            return False
        
    def get_by_model(self, model): #El listado de autos debe ser capaz de filtrar por modelo
        try:
            results = self.db_manager.execute_query(
                "SELECT * FROM lyfter_car_rental.cars WHERE model = %s;",
                model
            )
            formatted_result = [self._format_record(result) for result in results]
            return formatted_result
        except Exception as error:
            print("Error getting a car from the database: ", error)
            return False
    
    def get_by_id(self, id):
        try:
            
            results = self.db_manager.execute_query(
                "SELECT * FROM lyfter_car_rental.cars WHERE id = %s;",
                (id,)
            )
            formatted_result = [self._format_record(result) for result in results]
            return formatted_result
        except Exception as error:
            print("Error getting a car from the database: ", error)
            return False
        
    def change_status(self, id, status): #Cambiar el estado de un automovil
        try:
            self.db_manager.execute_query(
                "UPDATE lyfter_car_rental.cars SET status = %s WHERE id = %s",
                (status, id)
            )
            if self.db_manager.cursor.rowcount == 0:
                return {"success": False, "error": "car id not found"}
            print(f'Car status updated to {status} for car {id}')
            return {"success": True, "message": "Car status updated successfully", "id": id, "status": status}
        except Exception as error:
            print("Error updating car status: ", error)
            return {"success": False, "error": str(error)}      


class RentalRepository:
    def __init__(self, db_manager):
        self.db_manager = db_manager

    def _format_record(self, record):
        return {
            "id": record[0],
            "rental_date": record[1],
            "rental_status": record[2],
            "car_id": record[3],
            "user_id": record[4]
        }

    def create(self, car_id,user_id): #Crear un alquiler nuevo
        try:
            self.db_manager.execute_query(
                "INSERT INTO lyfter_car_rental.rentals (rental_status,car_id,user_id) VALUES ( 'reserved', %s, %s)",
                (car_id, user_id)
            )
            result = self.db_manager.execute_query("SELECT LASTVAL();")
            self.db_manager.execute_query(
                "UPDATE lyfter_car_rental.cars SET status = 'unavailable' WHERE id = %s",
                (car_id,)
            )
            new_id = result[0][0] if result else None
            print(f'Record created successfully')
            return {"success": True, "message": "Rental created successfully", "id": new_id}
        except Exception as error:
            print("Error inserting record into the database: ", error)
            return {"success": False, "error": str(error)}

    def get_all(self):
        try:
            results = self.db_manager.execute_query(
                "SELECT * FROM lyfter_car_rental.rentals;"
            )
            formatted_results = [self._format_record(result) for result in results]
            return formatted_results
        except Exception as error:
            print("Error getting all records from the database: ", error)
            return False

    def get_by_rental_status(self, rental_status): #El listado de alquileres debe ser capaz de filtrar por estado
        try:
            results = self.db_manager.execute_query(
                "SELECT * FROM lyfter_car_rental.rentals WHERE rental_status = %s;",
                (rental_status,)
            )
            formatted_results = [self._format_record(result) for result in results]
            return formatted_results
        except Exception as error:
            print("Error getting rentals from the database: ", error)
            return False
    
    def get_by_id(self, id):
        try:
            results = self.db_manager.execute_query(
                "SELECT * FROM lyfter_car_rental.rentals WHERE id = %s;",
                (id,)
            )
            formatted_results = [self._format_record(result) for result in results]
            return formatted_results
        except Exception as error:
            print("Error getting rental from the database: ", error)
            return False

    def complete_rental(self, id): #Completar un alquiler
        try:
            self.db_manager.execute_query(
                "UPDATE lyfter_car_rental.rentals SET rental_status = 'returned' WHERE id = %s",
                (id,)
            )
            self.db_manager.execute_query(
                "UPDATE lyfter_car_rental.cars SET status = 'available' WHERE id = (SELECT car_id FROM lyfter_car_rental.rentals WHERE id = %s)",
                (id,)
            )
            print("Rental has been completed successfully")
            return {"success": True, "message": "Rental has been completed successfully", "id": id, "rental_status": "returned"}
        except Exception as error:
            print("Error, unable to complete rental: ", error)
            return {"success": False, "error": str(error)}
        
    def change_rental_status(self, id, rental_status): #Cambiar el estado de un alquiler
        try:
            self.db_manager.execute_query(
                "UPDATE lyfter_car_rental.rentals SET rental_status = %s WHERE id = %s",
                (rental_status, id)
                )
            if rental_status.upper() == "RETURNED":
                self.db_manager.execute_query(
                "UPDATE lyfter_car_rental.cars SET status = 'available' WHERE id = (SELECT car_id FROM lyfter_car_rental.rentals WHERE id = %s)",
                (id,)
                )
            if rental_status.upper() == "IN USE" or rental_status.upper() == "RESERVED":
                self.db_manager.execute_query(
                "UPDATE lyfter_car_rental.cars SET status = 'unavailable' WHERE id = (SELECT car_id FROM lyfter_car_rental.rentals WHERE id = %s)",
                (id,)
                )
            print(f'Rental id {id} has been updated to {rental_status}')
            return {"success": True, "message": "Rental status updated successfully", "id": id, "rental_status": rental_status}
        except Exception as error:
            print("Error, unable to update rental status: ", error)
            return {"success": False, "error": str(error)}   