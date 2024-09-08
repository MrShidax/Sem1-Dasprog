def witch_riddle(numbers, b, c, indices):
    # Convert the input list of numbers to a list of integers
    numbers = list(map(int, numbers.split()))
    
    # Convert indices from string to list of integers
    indices = list(map(int, indices.split()))
    
    # Length of the list
    n = len(numbers)
    
    # Perform the cat jumps c times
    for _ in range(c):
        # Rotate the list by b positions
        numbers = numbers[-b:] + numbers[:-b]
    
    # Fetch the values at the specified indices
    result = [numbers[i] for i in indices if i < len(numbers)]
    
    # Print the result as space-separated values
    print(" ".join(map(str, result)))

# Read inputs from the user
numbers = input("Enter the list of numbers: ")
b = int(input("Enter the number of cats jumping each time: "))
c = int(input("Enter the number of jumps: "))
indices = input("Enter the indices separated by space: ")

witch_riddle(numbers, b, c, indices)