
numeros = []

for i in range(10):
    num = int(input(f"Ingrese el número {i + 1}: "))
    numeros.append(num)


def es_primo(num):
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True


mayor_primo = -1
posicion_mayor_primo = -1

# Recorremos la lista de números para buscar el mayor primo
for i in range(10):
    if es_primo(numeros[i]) and numeros[i] > mayor_primo:
        mayor_primo = numeros[i]
        posicion_mayor_primo = i

if mayor_primo != -1:
    print(f"El mayor número primo es {mayor_primo} y está en la posición {posicion_mayor_primo + 1}.")
else:
    print()