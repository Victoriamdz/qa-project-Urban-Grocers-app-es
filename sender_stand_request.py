import requests
import configuration
import data


# Crer usuario y devolver respuesta
def post_new_user(body):
    return requests.post(
        configuration.URL_SERVICE + configuration.CREATE_USER_PATH,
        json=body,
        headers=data.headers
    )

#Crear kit para usuario con token de autenticación
def post_new_client_kit(body, auth_token):
    headers_with_auth = data.headers.copy()
    headers_with_auth['Authorization'] = f"Bearer {auth_token}"

    return requests.post(
        configuration.URL_SERVICE + configuration.KITS_PATH,
        json=body,
        headers=headers_with_auth
    )
