import sender_stand_request
import data
import pytest

# Prueba: Crear usuario y kit
def test_create_kit():
    new_user_response = sender_stand_request.post_new_user(data.user_body)

    assert new_user_response.status_code == 201, "Error: No se pudo crear el usuario"

    auth_token = new_user_response.json().get('authToken')
    assert auth_token, "Error: No se recibió authToken"

    new_kit_response = sender_stand_request.post_new_client_kit(data.kit_body.copy(), auth_token)

    assert new_kit_response.status_code == 201, "Error: No se pudo crear el kit"
    assert new_kit_response.json().get("name") == data.kit_body["name"], "Error: El nombre del kit no coincide"

# PRUEBA 1: Número permitido de caracteres (1)
def test_create_kit_min_length():
    kit_data = data.kit_body.copy()
    kit_data["name"] = "a"
    new_user_response = sender_stand_request.post_new_user(data.user_body)
    auth_token = new_user_response.json().get('authToken')

    new_kit_response = sender_stand_request.post_new_client_kit(kit_data, auth_token)
    assert new_kit_response.status_code == 201
    assert new_kit_response.json().get("name") == kit_data["name"]

# PRUEBA 2: Número permitido de caracteres (511)
def test_create_kit_max_valid_length():
    kit_data = data.kit_body.copy()
    kit_data["name"] = "AbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdAbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabC"
# 511 caracteres
    new_user_response = sender_stand_request.post_new_user(data.user_body)
    auth_token = new_user_response.json().get('authToken')

    new_kit_response = sender_stand_request.post_new_client_kit(kit_data, auth_token)
    assert new_kit_response.status_code == 201
    assert new_kit_response.json().get("name") == kit_data["name"]

# PRUEBA 3: Número de caracteres es menor a lo permitido (0)
def test_create_kit_empty_name():
    kit_data = data.kit_body.copy()
    kit_data["name"] = ""
    new_user_response = sender_stand_request.post_new_user(data.user_body)
    auth_token = new_user_response.json().get('authToken')

    new_kit_response = sender_stand_request.post_new_client_kit(kit_data, auth_token)
    assert new_kit_response.status_code == 400

#PRUEBA 4: Número de caracteres es mayor que lo permitido (512)
def test_create_kit_too_long_name():
    kit_data = data.kit_body.copy()
    kit_data["name"] = "AbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdAbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcD"  # 512 caracteres
    new_user_response = sender_stand_request.post_new_user(data.user_body)
    auth_token = new_user_response.json().get('authToken')

    new_kit_response = sender_stand_request.post_new_client_kit(kit_data, auth_token)
    assert new_kit_response.status_code == 400

# PRUEBA 5: Se permiten caracteres especiales
def test_create_kit_special_chars():
    kit_data = data.kit_body.copy()
    kit_data["name"] = "!A%@#"
    new_user_response = sender_stand_request.post_new_user(data.user_body)
    auth_token = new_user_response.json().get('authToken')

    new_kit_response = sender_stand_request.post_new_client_kit(kit_data, auth_token)
    assert new_kit_response.status_code == 201
    assert new_kit_response.json().get("name") == kit_data["name"]

#PRUEBA 6: Se permiten espacios
def test_create_kit_spaces():
    kit_data = data.kit_body.copy()
    kit_data["name"] = " X xaa "
    new_user_response = sender_stand_request.post_new_user(data.user_body)
    auth_token = new_user_response.json().get('authToken')

    new_kit_response = sender_stand_request.post_new_client_kit(kit_data, auth_token)
    assert new_kit_response.status_code == 201
    assert new_kit_response.json().get("name") == kit_data["name"]

# PRUEBA 7: Se permiten números
def test_create_kit_numbers():
    kit_data = data.kit_body.copy()
    kit_data["name"] = "123"
    new_user_response = sender_stand_request.post_new_user(data.user_body)
    auth_token = new_user_response.json().get('authToken')

    new_kit_response = sender_stand_request.post_new_client_kit(kit_data, auth_token)
    assert new_kit_response.status_code == 201
    assert new_kit_response.json().get("name") == kit_data["name"]

# PRUEBA 8: El parámetro "name" no se pasa en la solicitud
def test_create_kit_no_name():
    kit_data = {}  # Sin parámetro "name"
    new_user_response = sender_stand_request.post_new_user(data.user_body)
    auth_token = new_user_response.json().get('authToken')

    new_kit_response = sender_stand_request.post_new_client_kit(kit_data, auth_token)
    assert new_kit_response.status_code == 400

# PRUEBA 9: Se pasa un tipo de parámetro diferente (número)
def test_create_kit_name_as_number():
    kit_data = data.kit_body.copy()
    kit_data["name"] = 123  # Número en lugar de string
    new_user_response = sender_stand_request.post_new_user(data.user_body)
    auth_token = new_user_response.json().get('authToken')

    new_kit_response = sender_stand_request.post_new_client_kit(kit_data, auth_token)
    assert new_kit_response.status_code == 400
