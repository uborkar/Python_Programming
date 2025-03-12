# Function with arbitrary keyword arguments (**kwargs)
def print_info(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")

# Main program
print_info(name="John", age=25, city="New York")
