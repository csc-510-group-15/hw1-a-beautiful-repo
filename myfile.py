def add_numbers(a, b):
    return a + b  
x, y = 10, 20
if __name__ == "__main__":
    result = add_numbers(x, y)
    print("The sum of x and y is:", result)

    # Intentional error: calling a function that doesn't exist
    difference = subtract_numbers(x, y)
    print("The difference between x and y is:", difference)