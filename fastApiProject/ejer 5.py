# Read 10 integers and store them in a list
numeros = []
for i in range(10):
    num = int(input(f"Enter integer number {i + 1}: "))
    numeros.append(num)

# Determine the largest number in the list
mayor = max(numeros)

# Count how many times the largest number occurs
repeticiones = numeros.count(mayor)

# Display the result
print(f"The largest number is: {mayor}")
print(f"The largest number occurs {repeticiones} times.")

