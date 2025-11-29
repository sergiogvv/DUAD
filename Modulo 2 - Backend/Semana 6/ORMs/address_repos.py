from sqlalchemy import text, insert, select, update, delete
from db import address_table


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