num1 = int(input("Ingresa el primer numero: "))
while True:
    num2 = int(input("Ingresa el segundo numero: "))
    if num2 != 0:
        break
    print("El segundo numero no puede ser cero. Intenta de nuevo.")

print(f"El primer numero es {num1} y el segundo es {num2}")
print(f"La suma de los numeros es {num1 + num2}")
print(f"La resta de los numeros es {num1 - num2}")
print(f"La multiplicacion de los numeros es {num1 * num2}")
print(f"La division de los numeros es {num1 / num2}")