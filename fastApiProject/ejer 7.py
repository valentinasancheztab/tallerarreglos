def sumadigitos(n):
    return sum(int(digit) for digit in str(abs(n)))


def main():
    numeros = []  # List to store the numbers entered by the user

    # Read 10 integers from the user
    for i in range(10):
        while True:
            try:
                # Prompt the user to enter an integer
                num = int(input(f"Enter integer number {i + 1}: "))
                numeros.append(num)  # Add the number to the list
                break  # Exit the loop if the number is valid
            except ValueError:
                # Error message if the input is not a valid integer
                print("Please enter a valid integer.")

    # Initialize variables to find the number with the highest digit sum
    maxsuma = -1
    posicionmax = -1

    # Iterate through each number in the list to find the one with the highest digit sum
    for i, num in enumerate(numeros):
        suma = sumadigitos(num)  # Calculate the digit sum of the current number
        if suma > max_suma:
            max_suma = suma  # Update the highest sum found
            posicion_max = i  # Update the position of the number with the highest sum

    # Print the number with the highest digit sum and its position in the list
    print(f"The number with the highest digit sum is {numeros[posicion_max]} at position {posicion_max}.")


if __name__ == "__main__":
    main()  # Execute the main function