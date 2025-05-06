# Validation of an e-mail with regular expressions #

import re


def validate_email(email):
    email_pattern = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"
    if re.match(email_pattern, email):
        return True
    else:
        return False


user_email = input("Insert the email to be validated: ")
valid = validate_email(user_email)
print(f"The email: {user_email} is {valid}")

# Validation of an e-mail with library email-validator #

# from email_validator import validate_email, EmailNotValidError
#
# def validar_correo(correo):
#     try:
#         resultado = validate_email(correo)
#         print(f"Correo válido: {resultado.email}")
#     except EmailNotValidError as e:
#         print(f"Correo inválido: {e}")
#
# # Pruebas
# validar_correo("usuario@gmail.com")
# validar_correo("mal@@dominio.com")
