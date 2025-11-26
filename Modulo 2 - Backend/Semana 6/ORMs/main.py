from db import engine
from repos import UserRepository, CarRepository, AddressRepository
from flask import Flask, request, jsonify
from logic import api_response, validate_user_payload, check_result_success, check_car_attributes, check_if_user_id_exists, check_if_car_id_exists, valid_user_columns, valid_car_columns, valid_address_columns, validate_address_payload, check_if_user_exists, check_if_car_exists, check_if_address_exists


app = Flask(__name__)


#CREATE
@app.route("/user", methods = ["POST"])
def create_user(): #Crear un usuario nuevo
    try:
        request_body = request.json
        user_repo = UserRepository(engine)
        validate_user_payload(request_body, user_repo)
        result = user_repo.create(**request_body)
        check_result_success(result)
        return api_response(message=result["message"], data={"id": result["id"]}), 201
    except ValueError as ex:
        return api_response(message= str(ex)), 400
    except Exception as ex:
        print(f"Unexpected error: {ex}")
        return api_response(message= "Unexpected error"), 500 #unexpected generic error with generic message

@app.route("/car", methods = ["POST"])
def create_car(): #Crear un automovil nuevo
    try:
        request_body = request.json
        car_repo = CarRepository(engine)
        check_car_attributes(request_body)
        result = car_repo.create(**request_body)
        check_result_success(result)
        return api_response(message=result["message"], data={"id": result["id"]}), 201
    except ValueError as ex:
        return api_response(message= str(ex)), 400
    except Exception as ex:
        print(f"Unexpected error: {ex}")
        return api_response(message= "Unexpected error"), 500 #unexpected generic error with generic message

@app.route("/address", methods = ["POST"])
def create_address(): #Crear una nueva direccion
    try:
        request_body = request.json
        address_repo = AddressRepository(engine)
        user_repo = UserRepository(engine)
        validate_address_payload(request_body, user_repo)
        result = address_repo.create(**request_body)
        check_result_success(result)
        return api_response(message=result["message"], data={"id": result["id"]}), 201
    except ValueError as ex:
        return api_response(message= str(ex)), 400
    except Exception as ex:
        print(f"Unexpected error: {ex}")
        return api_response(message= "Unexpected error"), 500 #unexpected generic error with generic message

#UPDATE
@app.route("/user", methods = ["PUT"])
def update_user(): #modificar usuario
    try:
        request_body = request.json
        user_repo = UserRepository(engine)
        validate_user_payload(request_body, user_repo)

        if not request.args: #si el request no tiene argumentos, lanzar excepcion
            return api_response(message="Missing required arguments"), 400
        column, value = next(iter(request.args.items()))
        valid_user_columns(column)
        check_if_user_exists(column, value, user_repo)

        result = user_repo.update(column,value,**request_body)
        check_result_success(result)
        return api_response(message=result["message"], data=result["updated"]), 200
    except ValueError as ex:
        return api_response(message= str(ex)), 400
    except Exception as ex:
        print(f"Unexpected error: {ex}")
        return api_response(message= "Unexpected error"), 500 #unexpected generic error with generic message

@app.route("/car", methods = ["PUT"])
def update_car(): #modificar carro
    try:
        request_body = request.json
        car_repo = CarRepository(engine)
        check_car_attributes(request_body)

        if not request.args: #si el request no tiene argumentos, lanzar excepcion
            return api_response(message="Missing required arguments"), 400
        column, value = next(iter(request.args.items()))
        valid_car_columns(column)
        check_if_car_exists(column, value, car_repo)

        result = car_repo.update(column, value, **request_body)
        check_result_success(result)
        return api_response(message=result["message"], data=result["updated"]), 200
    except ValueError as ex:
        return api_response(message= str(ex)), 400
    except Exception as ex:
        print(f"Unexpected error: {ex}")
        return api_response(message= "Unexpected error"), 500 #unexpected generic error with generic message

@app.route("/car", methods = ["PATCH"])
def link_to_user(): #Asociar un automóvil a un usuario
    try:
        car_repo = CarRepository(engine)
        user_repo = UserRepository(engine)
        if not request.args: #si el request no tiene argumentos, lanzar excepcion
            return api_response(message="Missing required arguments"), 400
        car_id, user_id = request.args.values()
        
        #check_if_car_exists("id",id, car_repo)
        #check_if_user_id_exists(user_id,user_repo)

        result = car_repo.link_to_user(car_id, user_id)
        check_result_success(result)

        return api_response(message=result["message"], data=result["updated"]), 200
    except ValueError as ex:
        return api_response(message=str(ex)), 400
    except Exception as ex:
        print(f"Unexpected error: {ex}")
        return api_response(message="Unexpected error"), 500 #unexpected generic error with generic message

@app.route("/address", methods = ["PUT"])
def update_address(): #modificar direccion
    try:
        request_body = request.json
        address_repo = AddressRepository(engine)
        user_repo = UserRepository(engine)
        validate_address_payload(request_body, user_repo)

        if not request.args: #si el request no tiene argumentos, lanzar excepcion
            return api_response(message="Missing required arguments"), 400
        column, value = next(iter(request.args.items()))
        valid_address_columns(column)
        check_if_address_exists(column, value, address_repo)

        result = address_repo.update(column, value, **request_body)
        check_result_success(result)
        return api_response(message=result["message"], data=result["updated"]), 200
    except ValueError as ex:
        return api_response(message= str(ex)), 400
    except Exception as ex:
        print(f"Unexpected error: {ex}")
        return api_response(message= "Unexpected error"), 500 #unexpected generic error with generic message


#READ
@app.route("/user", methods = ["GET"])
def get_users(): #Listar todos los usuarios
    try:
        user_repo = UserRepository(engine)
        if not request.args: #si el request no tiene argumentos, devolver toda la tabla de usuarios
            return api_response(user_repo.get_all(), "users")  
        column, value = next(iter(request.args.items()))
        valid_user_columns(column)
        result = user_repo.get_by_column(column, value)
        return api_response(result,"users")
    except ValueError as ex:
        return api_response(message=str(ex)), 400
    except Exception as ex:
        print(f"Unexpected error: {ex}")
        return api_response(message="Unexpected error"), 500 #unexpected generic error with generic message

@app.route("/car", methods = ["GET"])
def get_cars(): #Listar todos los automoviles
    try:
        car_repo = CarRepository(engine)
        if not request.args:
            return api_response(car_repo.get_all(), "cars") 
        column, value = next(iter(request.args.items()))
        valid_car_columns(column)
        result = car_repo.get_by_column(column, value)
        return api_response(result,"cars")
    except ValueError as ex:
        return api_response(message=str(ex)), 400
    except Exception as ex:
        print(f"Unexpected error: {ex}")
        return api_response(message="Unexpected error"), 500 #unexpected generic error with generic message

@app.route("/address", methods = ["GET"])
def get_addresses(): #Listar direcciones
    try:
        address_repo = AddressRepository(engine)
        if not request.args:
            return api_response(address_repo.get_all(), "addresses") 
        column, value = next(iter(request.args.items()))
        valid_address_columns(column)
        result = address_repo.get_by_column(column, value)
        return api_response(result,"addresses")
    except ValueError as ex:
        return api_response(message=str(ex)), 400
    except Exception as ex:
        print(f"Unexpected error: {ex}")
        return api_response(message="Unexpected error"), 500 #unexpected generic error with generic message

#DELETE
@app.route("/user", methods = ["DELETE"])
def delete_user(): #Eliminar usuario
    try:
        user_repo = UserRepository(engine)
        if not request.args: #si el request no tiene argumentos, lanzar excepcion
            return api_response(message="Missing required arguments"), 400
        column, value = next(iter(request.args.items()))
        valid_user_columns(column)
        check_if_user_exists(column, value, user_repo)
        result = user_repo.delete_record(column, value)
        check_result_success(result)
        return api_response(message=result["message"], data=result["deleted"]), 200
    except ValueError as ex:
        return api_response(message= str(ex)), 400
    except Exception as ex:
        print(f"Unexpected error: {ex}")
        return api_response(message= "Unexpected error"), 500 #unexpected generic error with generic message

@app.route("/car", methods = ["DELETE"])
def delete_car(): #Eliminar carro
    try:
        car_repo = CarRepository(engine)
        if not request.args: #si el request no tiene argumentos, lanzar excepcion
            return api_response(message="Missing required arguments"), 400
        column, value = next(iter(request.args.items()))
        valid_car_columns(column)
        check_if_car_exists(column, value, car_repo)
        result = car_repo.delete_record(column, value)
        check_result_success(result)
        return api_response(message=result["message"], data=result["deleted"]), 200
    except ValueError as ex:
        return api_response(message= str(ex)), 400
    except Exception as ex:
        print(f"Unexpected error: {ex}")
        return api_response(message= "Unexpected error"), 500 #unexpected generic error with generic message

@app.route("/address", methods = ["DELETE"])
def delete_address(): #Eliminar direccion
    try:
        address_repo = AddressRepository(engine)
        if not request.args: #si el request no tiene argumentos, lanzar excepcion
            return api_response(message="Missing required arguments"), 400
        column, value = next(iter(request.args.items()))
        valid_address_columns(column)
        check_if_address_exists(column, value, address_repo)
        result = address_repo.delete_record(column, value)
        check_result_success(result)
        return api_response(message=result["message"], data=result["deleted"]), 200
    except ValueError as ex:
        return api_response(message= str(ex)), 400
    except Exception as ex:
        print(f"Unexpected error: {ex}")
        return api_response(message= "Unexpected error"), 500 #unexpected generic error with generic message

if __name__ ==   "__main__":
    app.run(host="localhost", debug = True)




