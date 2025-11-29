from sqlalchemy import text, insert, select, update, delete
from db import user_table


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