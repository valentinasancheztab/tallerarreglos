# Create a list to store the numbers
numeros = []

# Read 10 integers from the user
print("Please enter 10 integers:")
for _ in range(10):
    while True:
        try:
            numero = int(input())
            numeros.append(numero)
            break
        except ValueError:
            print("Invalid input. Please enter an integer.")

# Calculate the integer average
promedio = sum(numeros) // len(numeros)  # Use // to obtain the integer average

# Check if the average is in the list
if promedio in numeros:
    print(f"The integer average {promedio} is in the list.")
else:
    print(f"The integer average {promedio} is not in the list.")



