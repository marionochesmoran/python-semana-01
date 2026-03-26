#intentos = 5
#numeroSecreto = 30
#acerto = False

#while intentos>0:
    #numero = int(input("Ingresa el numero secreto: "))
    #if numeroSecreto == numero:
        #acerto = True
        #break
    #elif numeroSecreto > numero:
        #print(f"Error!! El numero secreto es mayor")
        #intentos -= 1
    #else:
        #print(f"Error!! El numero secreto es menor")
        #intentos -=1
    #print(f"intentos restantes: {intentos}")

#if acerto == True:
    #print(f"Ganaste!! Numero acertado")
#else:
    #print(f"Perdiste!! Te quedaste sin intentos")

def juego():
    secreto = 34
    intentos = 5

    while intentos > 0:
        intento = pedir_numero()
        resultado = evaluar_intento(secreto,intento)
        if resultado == "correcto":
            print(f"el numero {intento} es {resultado}")
            break
        else:
            print(f"el numero secreto es {resultado} que {intento}")
            intentos -= 1
    
    if intentos ==0:
        print(f"No adivinaste el numero")

def pedir_numero():
    numero = int(input("Ingresa el numero secreto: "))
    return numero

def evaluar_intento(i,j):
    if i == j:
        return "correcto"
    elif i > j:
        return "mayor"
    else:
        return "menor"

juego()