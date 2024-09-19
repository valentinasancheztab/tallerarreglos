# Initialize an empty list to store the numbers
numeros = []

# Read 10 integers from the user
for i in range(10):
    numero = int(input(f"Enter integer number {i + 1}: "))
    numeros.append(numero)

# Print the entered numbers
print("Entered numbers:", numeros)

# Find and display the positions of numbers that end in 4
posiciones_terminan_en_4 = [i + 1 for i, num in enumerate(numeros) if num % 10 == 4]

# Print the positions
if posiciones_terminan_en_4:
    print("The positions of the numbers that end in 4 are:", posiciones_terminan_en_4)
else:
    print("There are no numbers that end in 4.")

