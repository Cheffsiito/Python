nombre = input("\033[1;31mNombre: \033[0m")
edad = input("\033[1;32mEdad: \033[0m")
email = input("\033[1;34mEmail: \033[0m")

mensaje = f"Mi nombre es \033[1;31m{nombre}\033[0m, tengo \033[1;32m{edad}\033[0m años y se enviará un correo electrónico a la siguiente dirección \033[1;34m{email}\033[0m."
print(mensaje)

