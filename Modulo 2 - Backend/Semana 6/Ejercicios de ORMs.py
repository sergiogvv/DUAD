from sqlalchemy import create_engine, text, MetaData, Table, Column, Integer, String, ForeignKey, insert, select, update, delete

DB_URI = "postgresql://postgres:admin@localhost:5432/postgres"
engine = create_engine(DB_URI, echo=True)

# Asociar metadata al schema
metadata_obj = MetaData(schema="semana6") #schema creado previamente

user_table = Table(
		"users",
		metadata_obj,
		Column("id", Integer, primary_key=True, autoincrement= "auto"),
        Column("full_name", String(50), nullable=False),
        Column("user_name", String(30), nullable=False),
        Column("password", String(20), nullable=False)
)

cars_table = Table(
		"cars",
		metadata_obj,
		Column("id", Integer, primary_key=True, autoincrement= "auto"),
        Column("user_id", ForeignKey("users.id")), #De esta manera declaramos una FK
        Column("car_make", String(30), nullable=False),
        Column("model", String(50), nullable=False),
        Column("year", Integer, nullable=False),
)

address_table = Table(
    "address",
    metadata_obj,
    Column("id", Integer, primary_key=True),
    Column("user_id", ForeignKey("users.id")), #De esta manera declaramos una FK
    Column("address", String, nullable=False)
)

metadata_obj.create_all(engine)

def format_record(record):
        return {
            "id": record[0],
            "full_name": record[1],
            "user_name": record[2],
            "password": record[3],
        }


stmt = select(user_table)

with engine.connect() as conn:
    results = conn.execute(stmt)

formatted_results = [format_record(result) for result in results]

print(formatted_results)
