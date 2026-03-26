cuentas = []

def administrar_propinas():
    while True:
        opcion= int(input("""
                                 Menú de propinas:
                                 1. Nueva cuenta
                                 2. Salir
                                 ... 
                                 """))
        while opcion not in [1, 2]:
            opcion = int(input("Opción no válida. Elige 1 o 2: "))

        if opcion == 1:
            nueva_cuenta()
        elif opcion ==2:
            resumen()
            break

def nueva_cuenta():
    valor_cuenta = int(input("Valor de la cuenta: "))
    porcentaje_propina = int(input("""
                                   Elige la propina escogida:
                                   1. 10%
                                   2. 15%
                                   3. 20%
                                   ... 
                                   """))
    while porcentaje_propina not in [1, 2, 3]:
            porcentaje_propina = int(input("Opción no válida. Elige 1, 2 o 3: "))
    
    if porcentaje_propina == 1:
         valor_propina = valor_cuenta * 10 / 100
    elif porcentaje_propina == 2:
         valor_propina = valor_cuenta * 15 / 100
    else:
         valor_propina = valor_cuenta * 20 / 100
    
    personas_pagan = int(input("¿Cuantas personas pagaran la cuenta?: "))

    cuenta = {
         "id": len(cuentas) + 1,
         "valor": valor_cuenta,
         "propina": valor_propina,
         "personas": personas_pagan
    }

    cuentas.append(cuenta)
    print(f"""
          El valor de la propina es {valor_propina}
          Total a pagar es {valor_cuenta + valor_propina}
          Personas a pagar {personas_pagan}. Pago por persona: {(valor_cuenta + valor_propina)/personas_pagan}
          """)

def resumen():
     for cuenta in cuentas:
        print(f"""
                  Cuenta N°: {cuenta['id']}
                  Valor: {cuenta['valor']}
                  Propina: {cuenta['propina']}
                  Pago total por persona: {(cuenta['valor']+cuenta['propina'])/cuenta['personas']}
                  -------
                  """)

administrar_propinas()