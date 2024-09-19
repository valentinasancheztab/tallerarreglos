# Function to check if a number is prime
def es_primo(num):
    # Numbers less than or equal to 1 are not prime
    if num <= 1:
        return False
    # Numbers 2 and 3 are prime
    if num <= 3:
        return True
    # Eliminate multiples of 2 and 3
    if num % 2 == 0 or num % 3 == 0:
        return False
    # Check possible factors from 5 up to the square root of the number
    i = 5
    while i * i <= num:
        # If the number is divisible by i or i + 2, it is not prime
        if num % i == 0 or num % (i + 2) == 0:
            return False
        # Check the next possible factors (i + 6)
        i += 6
    return True

# Function to obtain a list of prime numbers within a specific range
def obtener_primos_en_rango(inicio, fin, cantidad):
    primos = []  # List to store the found prime numbers
    # Iterate over each number in the specified range
    for num in range(inicio, fin + 1):
        # If the number is prime, add it to the list
        if es_primo(num):
            primos.append(num)
        # Stop when the desired amount of primes has been found
        if len(primos) == cantidad:
            break
    return primos

# Define the range and the number of prime numbers to find
inicio = 100
fin = 300
cantidad = 10

# Obtain the prime numbers in the specified range
primos = obtener_primos_en_rango(inicio, fin, cantidad)

# Display the found prime numbers on the screen
for primo in primos:
    print(primo)