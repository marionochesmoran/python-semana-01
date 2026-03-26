contactos = [
    {"nombre": "Ana", "telefono": "123456", "email": "ana@email.com"},
    {"nombre": "Carlos", "telefono": "789012", "email": "carlos@email.com"}
]
def juego():
    while True:
        opcion = int(input("""
            Menu de Agenda:
            1. Ver contactos
            2. Buscar contacto
            3. Agregar contacto
            4. Salir           
            """))
        
        while opcion not in [1, 2, 3, 4]:
            opcion = input("Opción no válida. Elige 1, 2, 3 o 4: ")

        if opcion == 1:
            ver_contactos()
        elif opcion == 2:
            nombre = input("Digita el nombre del contacto: ")
            buscar_contacto(nombre)
        elif opcion == 3:
            agregar_contacto()
        elif opcion == 4:
            break

def ver_contactos():
    for contacto in contactos:
        print(f"""
                  Nombre : {contacto['nombre']}
                  Teléfono : {contacto['telefono']}
                  Email : {contacto['email']}
                  """)

def buscar_contacto(nombre):
    for contacto in contactos:
        if contacto["nombre"]== nombre:
            print(f"""
                  Nombre : {contacto['nombre']}
                  Teléfono : {contacto['telefono']}
                  Email : {contacto['email']}
                  """)
            return        
    print(f"Contacto no encontrado")

def agregar_contacto():
    nombre = input("Nombre: ")
    telefono = input("Teléfono: ")
    email = input("Email: ")

    nuevo_contacto = {
        "nombre": nombre,
        "telefono": telefono,
        "email": email
    }   

    contactos.append(nuevo_contacto)
    print(f"Nuevo contacto {nombre} agregado a la agenda")   

juego() 
