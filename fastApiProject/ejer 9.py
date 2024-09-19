# Función para leer 10 números enteros
def leer_numeros(cantidad):
    numeros = []
    for i in range(cantidad):
        while True:
            try:
                # Prompt the user to enter an integer
                numero = int(input(f"Ingrese el número entero {i + 1}: "))
                numeros.append(numero)
                break # Exit the loop if input is valid
            except ValueError:
                print("Entrada inválida. Por favor, ingrese un número entero.")
    return numeros

# Función para mostrar los enteros comprendidos entre 1 y cada número en el arreglo
def mostrar_rango(numeros):
    for numero in numeros:
        print(f"\nEnteros comprendidos entre 1 y {numero}:")
        if numero < 1:
            print("No hay enteros en este rango.")
        else:
            for i in range(1, numero + 1):
                print(i, end=' ')
        print()  # Para salto de línea

# Read 10 integers from the user
numeros = leer_numeros(10)

# Display the integers between 1 and each number in the list
mostrar_rango(numeros)
