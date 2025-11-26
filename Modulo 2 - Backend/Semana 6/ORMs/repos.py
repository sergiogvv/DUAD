from sqlalchemy import create_engine, text, MetaData, Table, Column, Integer, String, ForeignKey, insert, select, update, delete
from db import metadata_obj, user_table, cars_table, address_table


class UserRepository:
    def __init__(self,engine):
        self.engine = engine
        

    def _format_record(self, record):
        return {
            "id": record[0],
            "full_name": record[1],
            "user_name": record[2],
            "password": record[3],
        }
    
    def create(self, full_name, user_name, password):
        try:
            stmt = insert(user_table).returning(user_table.c.id).values(full_name= full_name , user_name= user_name, password= password)
            with self.engine.connect() as conn:
                result = conn.execute(stmt)
                conn.commit()
                new_id = result.fetchall()[0][0] if result else None
                print(f'Record created successfully: user id: {new_id}')
                return {"success": True, "message": "User created successfully", "id": new_id}
        except Exception as error:
            print("Error inserting record into the database: ", error)
            return {"success": False, "error": str(error)}

    def get_all(self): #Listar todos los usuarios
        try:
            stmt = select(user_table)
            with self.engine.connect() as conn:
                results = conn.execute(stmt)
            formatted_results = [self._format_record(result) for result in results]
            return formatted_results
        except Exception as error:
            print("Error getting all records from the database: ", error)
            return False

    def get_by_column(self,column,value):
        try:
            with self.engine.connect() as conn:
                results = conn.execute(text(f"SELECT * FROM semana6.users WHERE {column} = {value}"))
            formatted_results = [self._format_record(result) for result in results]
            return formatted_results
        except Exception as error:
            print("Error getting records from the database: ", error)
            return False

    def get_by_id(self, id):
        try:
            stmt = select(user_table).where(user_table.c.id == id)
            with self.engine.connect() as conn:
                results = conn.execute(stmt)            
            formatted_result = [self._format_record(result) for result in results]
            return formatted_result
        except Exception as error:
            print("Error getting user from the database: ", error)
            return False

    def update(self, column,value, full_name: str, user_name: str, password: str):
        try:
            with self.engine.connect() as conn:
                results = conn.execute(text(f"SELECT * FROM semana6.users WHERE {column} = {value}"))
                update_result = conn.execute(text(f"UPDATE semana6.users SET full_name = '{full_name}', user_name = '{user_name}', password = '{password}' WHERE {column} = {value}"))
                conn.commit()
            formatted_results = [self._format_record(result) for result in results]
            return {"success": True, "message": "Update succesful", "updated": formatted_results["id"]}
        except Exception as error:
            print("Error updating user from the database: ", error)
            return False        


    def delete_record(self,column,value):
        try:
            with self.engine.connect() as conn:
                results = conn.execute(text(f"SELECT * FROM semana6.users WHERE {column} = {value}"))
                delete_result = conn.execute(text(f"DELETE FROM semana6.users WHERE {column} = {value}"))
                conn.commit()
            formatted_results = [self._format_record(result) for result in results]
            return {"success": True, "message": "Deletion succesful", "deleted": formatted_results}
        except Exception as error:
            print("Error deleting records from the database: ", error)
            return False


class CarRepository:
    def __init__(self,engine):
        self.engine = engine

    def _format_record(self, record):
        return {
            "id": record[0],
            "user_id": record[1],
            "car_make": record[2],
            "model": record[3],
            "year": record[4],
        }

    def create(self, car_make: str, model: str, year: int, user_id: int= None): #Crear un automovil nuevo
        try:
            stmt = insert(cars_table).returning(cars_table.c.id).values(user_id= user_id, car_make= car_make , model= model, year= year)
            with self.engine.connect() as conn:
                result = conn.execute(stmt)
                conn.commit()
            new_id = result.fetchall()[0][0] if result else None
            print(f'Record created successfully: car id: {new_id}')
            return {"success": True, "message": "Car created successfully", "id": new_id}
        except Exception as error:
            print("Error inserting record into the database: ", error)
            return {"success": False, "error": str(error)}
        
    def get_all(self): #Listar todos los automoviles
        try:
            stmt = select(cars_table)
            with self.engine.connect() as conn:
                results = conn.execute(stmt)
            formatted_results = [self._format_record(result) for result in results]
            return formatted_results
        except Exception as error:
            print("Error getting all records from the database: ", error)
            return False

    def get_by_column(self,column,value):
        try:
            with self.engine.connect() as conn:
                results = conn.execute(text(f"SELECT * FROM semana6.cars WHERE {column} = {value}"))
            formatted_results = [self._format_record(result) for result in results]
            return formatted_results
        except Exception as error:
            print("Error getting records from the database: ", error)
            return False

    def update(self, column,value, car_make: str, model: str, year: int, user_id: int):
        try:
            with self.engine.connect() as conn:
                results = conn.execute(text(f"SELECT * FROM semana6.cars WHERE {column} = {value}"))
                update_result = conn.execute(text(f"UPDATE semana6.cars SET car_make = '{car_make}', model = '{model}', year = {year}, user_id = {user_id} WHERE {column} = {value}"))
                conn.commit()
            formatted_results = [self._format_record(result) for result in results]
            return {"success": True, "message": "Update succesful", "updated": formatted_results}
        except Exception as error:
            print("Error updating user from the database: ", error)
            return False

    def link_to_user(self, id: int, user_id: int): #Asociar un automóvil a un usuario
        try:
            stmt1 = (
                update(cars_table)
                .where(cars_table.c.id == id)
                .values(user_id= user_id)
            )
            stmt2 = select(cars_table).where(cars_table.c.id == id)      
            with self.engine.connect() as conn:
                conn.execute(stmt1)
                results= conn.execute(stmt2) 
                conn.commit()
            formatted_results = [self._format_record(result) for result in results]
            print(f'Record updated successfully')
            return {"success": True, "message": "Car succesfuly linked to user", "updated": formatted_results}
        except Exception as error:
            print("Error updating user from the database: ", error)
            return False 

    def delete_record(self,column,value):
        try:
            with self.engine.connect() as conn:
                results = conn.execute(text(f"SELECT * FROM semana6.cars WHERE {column} = {value}"))
                delete_result = conn.execute(text(f"DELETE FROM semana6.cars WHERE {column} = {value}"))
                conn.commit()
            formatted_results = [self._format_record(result) for result in results]
            return {"success": True, "message": "Deletion succesful", "deleted": formatted_results}
        except Exception as error:
            print("Error deleting records from the database: ", error)
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


class AddressRepository:
    def __init__(self,engine):
        self.engine = engine

    def _format_record(self, record):
        return {
            "id": record[0],
            "user_id": record[1],
            "address": record[2],
        }
    
    def create(self, user_id, address):
        try:
            stmt = insert(address_table).returning(address_table.c.id).values(user_id= user_id, address= address)
            with self.engine.connect() as conn:
                result = conn.execute(stmt)
                conn.commit()
            new_id = result.fetchall()[0][0] if result else None
            print(f'Record created successfully: car id: {new_id}')
            return {"success": True, "message": "Address created successfully", "id": new_id}
        except Exception as error:
            print("Error inserting record into the database: ", error)
            return {"success": False, "error": str(error)}

    def get_all(self): #Listar todas las direcciones
        try:
            stmt = select(address_table)
            with self.engine.connect() as conn:
                results = conn.execute(stmt)
            formatted_results = [self._format_record(result) for result in results]
            return formatted_results
        except Exception as error:
            print("Error getting all records from the database: ", error)
            return False

    def get_by_column(self,column,value):
        try:
            with self.engine.connect() as conn:
                results = conn.execute(text(f"SELECT * FROM semana6.addresses WHERE {column} = {value}"))
            formatted_results = [self._format_record(result) for result in results]
            return formatted_results
        except Exception as error:
            print("Error getting records from the database: ", error)
            return False

    def update(self,column, value, user_id: int, address: str ):
        try:
            with self.engine.connect() as conn:
                results = conn.execute(text(f"SELECT * FROM semana6.addresses WHERE {column} = {value}"))
                update_result = conn.execute(text(f"UPDATE semana6.addresses SET user_id = {user_id}, address = '{address}' WHERE {column} = {value}"))
                conn.commit()
            formatted_results = [self._format_record(result) for result in results]
            return {"success": True, "message": "Update succesful", "updated": formatted_results}
        except Exception as error:
            print("Error updating address from the database: ", error)
            return False



    def delete_record(self,column,value):
        try:
            with self.engine.connect() as conn:
                results = conn.execute(text(f"SELECT * FROM semana6.addresses WHERE {column} = {value}"))
                delete_result = conn.execute(text(f"DELETE FROM semana6.addresses WHERE {column} = {value}"))
                conn.commit()
            formatted_results = [self._format_record(result) for result in results]
            return {"success": True, "message": "Deletion succesful", "deleted": formatted_results}
        except Exception as error:
            print("Error deleting records from the database: ", error)
            return False