# Input height of the triangle
A = int(input("Enter the height of the Pascal's Triangle: "))

# Loop to generate each row
for i in range(A):
    number = 1  # The first number in every row is always 1
    
    # Print spaces for centering
    print(' ' * (A - i), end='')
    
    # Loop to print each element in the row
    for j in range(i + 1):
        print(number, end=' ')  # Print the number followed by a space
        number = number * (i - j) // (j + 1)  # Compute the next number using binomial coefficient formula
    
    print()  # Move to the next line after each row