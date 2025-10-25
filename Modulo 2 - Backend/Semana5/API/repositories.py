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

    def get_all(self):
        try:
            results = self.db_manager.execute_query(
                "SELECT * FROM lyfter_car_rental.users;"
            )
            formatted_results = [self._format_record(result) for result in results]
            return formatted_results
        except Exception as error:
            print("Error getting all records from the database: ", error)
            return False
        
    def create(self, full_name, email, username, password, DOB, account_status):
        try:
            self.db_manager.execute_query(
                "INSERT INTO lyfter_car_rental.users (full_name, email, username, password, DOB, account_status) VALUES (%s, %s, %s, %s, %s, %s)",
                (full_name, email, username, password, DOB, account_status)
            )
            print("Record inserted successfully")
            return True
        except Exception as error:
            print("Error inserting record into the database: ", error)
            return False
    


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

    def get_all(self):
        try:
            results = self.db_manager.execute_query(
                "SELECT * FROM lyfter_car_rental.cars;"
            )
            formatted_results = [self._format_record(result) for result in results]
            return formatted_results
        except Exception as error:
            print("Error getting all records from the database: ", error)
            return False
        
    def create(self, car_make, model, year):
        try:
            self.db_manager.execute_query(
                "INSERT INTO lyfter_car_rental.cars (car_make, model, year) VALUES (%s, %s, %s)",
                (car_make, model, year)
            )
            print("Record inserted successfully")
            return True
        except Exception as error:
            print("Error inserting record into the database: ", error)
            return False
    

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
        
    def create(self, rental_status,car_id,user_id):
        try:
            self.db_manager.execute_query(
                "INSERT INTO lyfter_car_rental.rentals (rental_status,car_id,user_id) VALUES (%s, %s, %s)",
                (rental_status,car_id,user_id)
            )
            self.db_manager.execute_query(
                "UPDATE lyfter_car_rental.cars SET status = 'unavailable' WHERE id = %s",
                (car_id)
            )
            print("Record inserted successfully")
            return True
        except Exception as error:
            print("Error inserting record into the database: ", error)
            return False
    


