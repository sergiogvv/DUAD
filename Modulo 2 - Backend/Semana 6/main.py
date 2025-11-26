from db import engine
from repos import UserRepository, CarRepository, AddressRepository
from flask import Flask, request, jsonify
from os import path
from logic import api_response, validate_user_payload, check_result_success, check_car_attributes, check_if_user_id_exists, check_if_car_id_exists, valid_user_columns, valid_car_columns, valid_address_columns, validate_address_payload, check_if_user_exists


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
@app.route("/user", methods = ["PATCH"])
def update_user_status(): #Cambiar el estado de un usuario
    try:
        request_body = request.json
        user_repo = UserRepository(engine)

        check_if_user_id_exists(request_body["id"], user_repo)
        # is_valid_account_status(request_body["account_status"])

        result = user_repo.change_account_status(**request_body)
        check_result_success(result)
        return api_response(message=result["message"], data={"id": result["id"], "account_status": result["account_status"]}), 200
    except ValueError as ex:
        return api_response(message= str(ex)), 400
    except Exception as ex:
        print(f"Unexpected error: {ex}")
        return api_response(message= "Unexpected error"), 500 #unexpected generic error with generic message


@app.route("/car", methods = ["PATCH"])
def update_car_status(): #Cambiar el estado de un automovil
    try:
        request_body = request.json
        car_repo = CarRepository(engine)
        check_if_car_id_exists(request_body["id"], car_repo)
        # is_valid_car_status(request_body["status"])

        result = car_repo.change_status(**request_body)
        check_result_success(result)
        return api_response(message=result["message"], data={"id": result["id"], "status": result["status"]}), 200
    except ValueError as ex:
        return api_response(message= str(ex)), 400
    except Exception as ex:
        print(f"Unexpected error: {ex}")
        return api_response(message= "Unexpected error"), 500 #unexpected generic error with generic message


# @app.route("/rental_complete/<rental_id>", methods = ["PATCH"])
# def rental_complete(rental_id): #Completar un alquiler
#     try:
#         rental_repo = RentalRepository(engine)
#         check_if_rental_id_exists(rental_id, rental_repo)
#         result = rental_repo.complete_rental(rental_id)

#         check_result_success(result)
#         return api_response(message=result["message"], data={"id": result["id"]}), 200
#     except ValueError as ex:
#         return api_response(message= str(ex)), 400
#     except Exception as ex:
#         print(f"Unexpected error: {ex}")
#         return api_response(message= "Unexpected error"), 500 #unexpected generic error with generic message


# @app.route("/rental", methods = ["PATCH"])
# def update_rental_status(): #Cambiar el estado de un alquiler
#     try:
#         request_body = request.json
#         rental_repo = RentalRepository(engine)

#         check_if_rental_id_exists(request_body["id"],rental_repo)
#         is_valid_rental_status(request_body["rental_status"])

#         result = rental_repo.change_rental_status(**request_body)
#         check_result_success(result)
#         return api_response(message=result["message"], data={"id": result["id"]}), 200
#     except ValueError as ex:
#         return api_response(message= str(ex)), 400
#     except Exception as ex:
#         print(f"Unexpected error: {ex}")
#         return api_response(message= "Unexpected error"), 500 #unexpected generic error with generic message


@app.route("/user_defaulted/<user_id>", methods = ["PATCH"])
def user_defaulted(user_id): #Flagear un usuario como moroso
    try:
        user_repo = UserRepository(engine)
        check_if_user_id_exists(user_id, user_repo)
        result = user_repo.change_account_status(user_id, "defaulted")
        check_result_success(result)
        return api_response(message=result["message"], data={"id": result["id"], "account_status": result["account_status"]}), 200
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
        result = user_repo.delete_user(column, value)
        check_result_success(result)
        return api_response(message=result["message"], data=result["deleted"]), 200
    except ValueError as ex:
        return api_response(message= str(ex)), 400
    except Exception as ex:
        print(f"Unexpected error: {ex}")
        return api_response(message= "Unexpected error"), 500 #unexpected generic error with generic message

if __name__ ==   "__main__":
    app.run(host="localhost", debug = True)




