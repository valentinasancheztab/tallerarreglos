# We initialize the array as an empty list
numbers = []

# Read 10 numbers entered by the user
for i in range(10):
    # Define as float to accommodate numbers with decimal points
    num = float(input(f"Enter number {i + 1}: "))
    numbers.append(num)

# Find the maximum number and its position within the array
mayor_numero = max(numbers)
posicion_mayor = numbers.index(mayor_numero)

# Display the result
print(f"The largest number is {mayor_numero} and is located at position {posicion_mayor + 1}.")