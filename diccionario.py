persona = {
    "nombre" : "carlos",
    "edad" : 32,
    "ocupacion" : "desarrollador",
    "activo" : True
}

print(persona["nombre"])
print(persona.get("telefono","no tiene telefono"))

persona["email"] = "carlos@email.com"

for clave, valor in persona.items():
    print(f"{clave}: {valor}")
