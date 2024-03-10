correo_electronico = input("¿Cuál es tu dirección de correo electrónico?: ").strip()

nombre_usuario = correo_electronico[:correo_electronico.index("@")]

nombre_dominio = correo_electronico[correo_electronico.index("@")+1:]

resultado = "Tu nombre de usuario es '{}' y tu nombre de dominio es '{}'".format(nombre_usuario, nombre_dominio)

print(resultado)
