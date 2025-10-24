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
            "account_status": record[5]
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


