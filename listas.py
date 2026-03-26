frutas = ["manzana","pera","uva","mango"]

print(frutas[0])
print(frutas[-1])
print(len(frutas))

frutas.append("kiwi")
frutas.remove("pera")

for frutas in frutas:
    print(f"- {frutas.upper()}")