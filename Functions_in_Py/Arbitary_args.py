# Function with arbitrary positional arguments (*args)
def print_numbers(*args):
    for num in args:
        print(num)

# Main program
print_numbers(1, 2, 3, 4, 5)  # You can pass as many numbers as you want


