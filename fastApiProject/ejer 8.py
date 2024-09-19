import math

def leernumeros(cantidad):
    numeros = []
    for i in range(cantidad):
        while True:
            try:
                # Prompt the user to enter a number
                numero = int(input(f"Introduce el número {i + 1}: "))
                numeros.append(numero)
                break # Exit the loop if input is valid
            except ValueError:
                print("Entrada no válida. Por favor, introduce un número entero.")
    return numeros


def calcular_factoriales(numeros):
    factoriales = [math.factorial(num) for num in numeros]
    return factoriales


def mostrar_resultados(numeros, factoriales):
    for i in range(len(numeros)):
        print(f"El factorial de {numeros[i]} es {factoriales[i]}")

def main():
    cantidad = 10  # Specify the number of integers to read
    numeros = leernumeros(cantidad) # Read integers from the user
    factoriales = calcular_factoriales(numeros)# Calculate factorials
    mostrar_resultados(numeros, factoriales)# Display results

if __name__ == "__main__":  # Execute the main function
    main()