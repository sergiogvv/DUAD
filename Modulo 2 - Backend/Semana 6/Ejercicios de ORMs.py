from sqlalchemy import create_engine, text, MetaData, Table, Column, Integer, String, ForeignKey, insert, select, update, delete


DB_URI = 'postgresql://postgres:admin@localhost:5432/postgres'
engine = create_engine(DB_URI, echo=True)

try:
    connection = engine.connect()
    print("Connection successful!")
    connection.close()  # Cerramos la conexion cuando terminamos
except Exception as e:
    print("Connection failed:", e)


with engine.connect() as conn:
	result = conn.execute(text("SELECT 'hello world'"))
	print(result.all()) # [('hello world',)]
	
	users = conn.execute(text("SELECT * FROM users"))
	print(users.all()) # [(1, "John Doe", "jdoe@email.com")]