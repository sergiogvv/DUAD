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
    Column("email_address", String, nullable=False)
)

metadata_obj.create_all(engine)

with engine.connect() as conn:
    result = conn.execute(
        insert(user_table),
        [
            {"full_name": "Donny Gomar","user_name": "dgomar0","password": "mN8%qDrx"}, 
            {"full_name": "Carling Gerardin","user_name": "cgerardin1","password": "xR8_jE6\"C"}, 
            {"full_name": "Elke Laughlin","user_name": "elaughlin2","password": "nE4({fl%<&f|"}, 
            {"full_name": "Kelsi Mularkey","user_name": "kmularkey3","password": "fO8.8Dn8)!9i~Xv"}, 
            {"full_name": "Dov Marian","user_name": "dmarian4","password": "zJ9.P(p1K+M*>"}, 
            {"full_name": "Alberta Winchcomb","user_name": "awinchcomb5","password": "rD3<\"x18o=ISf6"}, 
            {"full_name": "Lizzie Siman","user_name": "lsiman6","password": "fN5.?|jlGsF#>*"}, 
            {"full_name": "Carena Bakeup","user_name": "cbakeup7","password": "bW7!N%bU@KiJ"}, 
            {"full_name": "Lissi Jennions","user_name": "ljennions8","password": "zN4`.bu.>R"}, 
            {"full_name": "Jessika Fancet","user_name": "jfancet9","password": "qT3=A.N/"}
        ]
    )
    conn.commit()

with engine.connect() as conn:
    result = conn.execute(
        insert(cars_table),
        [
            {"car_make": "Chevrolet", "model": "Corvette","year": 1993}, 
            {"car_make": "BMW","model": "Z4 M","year": 2006}, 
            {"car_make": "Hyundai","model": "Tiburon","year": 2007}, 
            {"car_make": "Volkswagen","model": "Jetta","year": 2004}, 
            {"car_make": "Maserati","model": "228","year": 1990}, 
            {"car_make": "Ford","model": "E-Series","year": 2002}, 
            {"car_make": "Buick","model": "Park Avenue","year": 2000}, 
            {"car_make": "Chevrolet","model": "HHR","year": 2009}, 
            {"car_make": "Dodge","model": "Caliber","year": 2012}, 
            {"car_make": "Dodge","model": "Ram 1500","year": 2009}
        ]
    )
    conn.commit()

with engine.connect() as conn:
    result = conn.execute(
        insert(address_table),
        [
            {"user_id": 1,"email_address": "dgomar0@gmail.com"}, 
            {"user_id": 2,"email_address": "cgerardin1@destro.org"}, 
            {"user_id": 3,"email_address": "elaughlin2@signal.com"}, 
            {"user_id": 4,"email_address": "kmularkey3@aol.com"}, 
            {"user_id": 5,"email_address": "dmarian4@udemy.com"}, 
            {"user_id": 6,"email_address": "awinchcomb5@gmail.com"}, 
            {"user_id": 7,"email_address": "lsiman6@outlook.com"}, 
            {"user_id": 8,"email_address": "cbakeup7@gmail.com"}, 
            {"user_id": 9,"email_address": "ljennions8@hotmail.com"}, 
            {"user_id": 10,"email_address": "jfancet9@hotmail.com",}            
        ]
    )
    conn.commit()
